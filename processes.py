from __future__ import division
from __future__ import print_function

# -*- coding: utf-8 -*-
# Copyright 2020 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections

import models


Process = collections.namedtuple(
    'Process',
    'name, description, applicability, stages')
# Note: A new feature always starts with intent_stage == INTENT_NONE
# regardless of process.  intent_stage is set to the first stage of
# a specific process when the user clicks a "Start" button and submits
# a form that sets intent_stage.


ProcessStage = collections.namedtuple(
    'ProcessStage',
    'name, description, progress_items, incoming_stage, outgoing_stage')


def process_to_dict(process):
  """Return nested dicts for the nested namedtuples of a process."""
  process_dict = {
      'name': process.name,
      'description': process.description,
      'applicability': process.applicability,
      'stages': [stage._asdict() for stage in process.stages],
  }
  return process_dict


BLINK_PROCESS_STAGES = [
  ProcessStage(
      'Start incubation',
      'Create an initial WebStatus feature entry and kick off standards '
      'incubation (WICG) to share ideas.',
      ['WICG discourse post',
       'Spec repo',
      ],
      models.INTENT_NONE, models.INTENT_IMPLEMENT),

  ProcessStage(
      'Start prototyping',
      'Share an explainer doc and API. '
      'Start prototyping code in a public repo.',
      ['Explainer',
       'API design',
       'Code in repo',
       'Security review',
       'Privacy review',
       'Intent to Prototype email',
       'Spec reviewer',
      ],
      models.INTENT_IMPLEMENT, models.INTENT_EXPERIMENT),

  ProcessStage(
      'Dev trials and iterate on design',
      'Publicize availablity for developers to try. '
      'Provide sample code. '
      'Request feedback from browser vendors.',
      ['Samples',
       'Draft API overview',
       'Request signals',
       'External reviews',
       'Ready for Trial email',
      ],
      models.INTENT_EXPERIMENT, models.INTENT_IMPLEMENT_SHIP),

  ProcessStage(
      'Evaluate readiness to ship',
      'Work through a TAG review and gather vendor signals.',
      ['TAG review request',
       'Vendor signals',
       'Documentation signoff',
       'Estimated target milestone',
      ],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_SHIP),

  ProcessStage(
      '(Optional) Origin Trial',
      'Set up and run an origin trial. '
      'Act on feedback from partners and web developers.',
      ['OT request',
       'OT available',
       'OT results',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone. Finalize docs and announcements. '
      'Further standardization.',
      ['Intent to Ship email',
       'Request to migrate incubation',
       'TAG issues addressed',
       'Three LGTMs',
       'Updated vendor signals',
       'Finalized target milestone',
      ],
      models.INTENT_SHIP, models.INTENT_REMOVE),
  ]


BLINK_LAUNCH_PROCESS = Process(
    'New feature incubation',
    'Description of blink launch process',  # Not used yet.
    'When to use it',  # Not used yet.
    BLINK_PROCESS_STAGES)


BLINK_FAST_TRACK_STAGES = [
  ProcessStage(
      'Identify feature',
      'Create an initial WebStatus feature entry to implement part '
      'of an existing specification or combinaton of specifications.',
      ['Spec links',
      ],
      models.INTENT_NONE, models.INTENT_IMPLEMENT_SHIP),

  ProcessStage(
      'Implement',
      'Check code into Chromium under a flag.',
      ['Code in Chromium',
      ],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_SHIP),

  ProcessStage(
      'Dev trials and iterate on implementation',
      'Publicize availablity for developers to try. '
      'Provide sample code. '
      'Act on feedback from partners and web developers.',
      ['Samples',
       'Draft API overview (may be on MDN)',
       'Ready for Trial email',
       'Estimated target milestone',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      '(Optional) Origin Trial',
      'Set up and run an origin trial. '
      'Act on feedback from partners and web developers.',
      ['OT request',
       'OT available',
       'OT results',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone. Finalize docs and announcements. '
      'Further standardization.',
      ['Intent to Ship email',
       'Three LGTMs',
       'Documentation signoff',
       'Finalized target milestone',
      ],
      models.INTENT_SHIP, models.INTENT_REMOVE),
  ]


BLINK_FAST_TRACK_PROCESS = Process(
    'Existing feature implementation',
    'Description of blink fast track process',  # Not used yet.
    'When to use it',  # Not used yet.
    BLINK_FAST_TRACK_STAGES)


PSA_ONLY_STAGES = [
  ProcessStage(
      'Identify feature',
      'Create an initial WebStatus feature entry for a web developer '
      'facing change to existing code.',
      ['Spec links',
      ],
      models.INTENT_NONE, models.INTENT_IMPLEMENT_SHIP),

  ProcessStage(
      'Implement',
      'Check code into Chromium under a flag.',
      ['Code in Chromium',
      ],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_SHIP),

  ProcessStage(
      'Dev trials and iterate on implementation',
      'Publicize availablity for developers to try. '
      'Act on feedback from partners and web developers.',
      ['Ready for Trial email',
       'Estimated target milestone',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone.',
      ['Web facing PSA email',
       'One LGTM',
       'Finalize target Milestone',
      ],
      models.INTENT_SHIP, models.INTENT_REMOVE),
  ]

PSA_ONLY_PROCESS = Process(
    'Web developer facing change to existing code',
    'Description of PSA process',   # Not used yet.
    'When to use it',  # Not used yet.
    PSA_ONLY_STAGES)


DEPRECATION_STAGES = [
  ProcessStage(
      'Identify feature',
      'Create an initial WebStatus feature entry to deprecate '
      'an existing feature stating impact.',
      ['Link to existing feature',
      ],
      models.INTENT_NONE, models.INTENT_IMPLEMENT_SHIP),

  ProcessStage(
      'Implement',
      'Move existing Chromium code under a flag.',
      ['Code in Chromium',
      ],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_SHIP),

  # TODO(cwilso): Work out additional steps for flag defaulting to disabled.
  ProcessStage(
      'Dev trial',
      'Publicize deprecation. ',
      ['Ready for Trial email',
       'Estimated target milestone',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to unship',
      'Lock in shipping milestone. Finalize docs and announcements. '
      'Further standardization.',
      ['Intent to Ship email',
       'Three LGTMs',
       'Finalized target milestone',
      ],
      models.INTENT_SHIP, models.INTENT_REMOVE),

  ProcessStage(
      '(Optional) Reverse Origin Trial',
      'Set up and run a reverse origin trial. ',
      ['ROT request',
       'ROT available',
       'Removal of ROT',
       'Removal of implementation code',
      ],
      models.INTENT_EXTEND_TRIAL, models.INTENT_EXTEND_TRIAL),
  ]


DEPRECATION_PROCESS = Process(
    'Feature deprecation',
    'Description of deprecation process',  # Not used yet.
    'When to use it',  # Not used yet.
    DEPRECATION_STAGES)


ALL_PROCESSES = {
    models.FEATURE_TYPE_INCUBATE_ID: BLINK_LAUNCH_PROCESS,
    models.FEATURE_TYPE_EXISTING_ID: BLINK_FAST_TRACK_PROCESS,
    models.FEATURE_TYPE_CODE_CHANGE_ID: PSA_ONLY_PROCESS,
    models.FEATURE_TYPE_DEPRECATION_ID: DEPRECATION_PROCESS,
    }

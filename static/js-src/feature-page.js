(function(exports) {
// Event handler. Used in feature.html template.
const subscribeToFeature = (featureId) => {
  const iconEl = document.querySelector('.pushicon');
  if (iconEl.icon === 'chromestatus:star') {
    StarService.setStar(featureId, false).then(() => {
      iconEl.icon = 'chromestatus:star-border';
    });
  } else {
    StarService.setStar(featureId, true).then(() => {
      iconEl.icon = 'chromestatus:star';
    });
  }
};

// Event handler. Used in feature.html template.
const shareFeature = () => {
  if (navigator.share) {
    const url = '/feature/' + FEATURE_ID;
    navigator.share({
      title: FEATURE_NAME,
      text: FEATUER_SUMMARY,
      url: url,
    }).then(() => {
      ga('send', 'social',
        {
          'socialNetwork': 'web',
          'socialAction': 'share',
          'socialTarget': url,
        });
    });
  }
};

// Remove loading spinner at page load.
document.body.classList.remove('loading');

// Unhide "Web Share" feature if browser supports it.
if (navigator.share) {
  Array.from(document.querySelectorAll('.no-web-share')).forEach((el) => {
    el.classList.remove('no-web-share');
  });
}

// Show the star icon if the user has starred this feature.
StarService.getStars().then((subscribedFeatures) => {
  const iconEl = document.querySelector('.pushicon');
  if (subscribedFeatures.includes(Number(FEATURE_ID))) {
    iconEl.icon = 'chromestatus:star';
  } else {
    iconEl.icon = 'chromestatus:star-border';
  }
});


if (SHOW_TOAST) {
  setTimeout(() => {
    const toastEl = document.querySelector('chromedash-toast');
    toastEl.showMessage('Your feature was saved! It may take a few minutes to ' +
                      'show up in the main list.', null, null, -1);
  }, 500);
}

exports.subscribeToFeature = subscribeToFeature;
exports.shareFeature = shareFeature;
})(window);

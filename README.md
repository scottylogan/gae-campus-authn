# Google App Engine Campus Authentication Test

This is a simple GAE python app to test campus authentication.  It works in one of two ways, depending on the App Engine configuration.

## Google Apps Domain

To authenticate with a specific Google Apps domain:

* set *Authentication Type* to _Google Apps domain_ in the *Application Settings* page
* set *Authentication Domain* to your base Google Apps domain name (e.g. _example.com_)
* have your Google Apps administrator approve the app for your domain


## Google Accounts API

To authenticate with any Google Account:

* set *Authentication Type* to _Google Accounts API_ in the *Application Settings* page

You can restrict access to specific domains by having your app check the domain component of a user's nickname or email address, or by checking the *USER_ORGANIZATION* environment variable (see [https://developers.google.com/appengine/articles/auth](https://developers.google.com/appengine/articles/auth) for details)



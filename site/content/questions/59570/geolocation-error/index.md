+++
type = "question"
title = "Geolocation error"
description = '''I have contributed to OSM for seven years. Now, for the first time, North America shows upon opening as here: https://www.openstreetmap.org/#map=5/38.007/-95.844. I receive messages such as below when I choose &#x27;Show my location&#x27;: Geolocation error: Network location provider at &#x27;https://www.googleapis...'''
date = "2017-09-12T15:19:00Z"
lastmod = "2018-10-02T23:31:00Z"
weight = 59570
keywords = [ "geolocation", "error" ]
aliases = [ "/questions/59570" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Geolocation error](/questions/59570/geolocation-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59570-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have contributed to OSM for seven years. Now, for the first time, North America shows upon opening as here: <a href="https://www.openstreetmap.org/#map=5/38.007/-95.844.">https://www.openstreetmap.org/#map=5/38.007/-95.844.</a> I receive messages such as below when I choose 'Show my location': Geolocation error: Network location provider at 'https://www.googleapis.com/' : Returned error code 403.. Geolocation error: Only secure origins are allowed (see: <a href="https://goo.gl/Y0ZkNV)..">https://goo.gl/Y0ZkNV)..</a> I am unaware of any action on my part to deny my location. I use a version of Chrome on my Windows desktop. I have read to go to Settings&gt;Content Settings...&gt;Website Settings&gt;openstreetmap.org. Website Settings does not exist so far as I can see.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '17, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59570" class="comments-container">
<span id="59571"></span>
<div id="comment-59571" class="comment">
<div id="post-59571-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It could be that you need to use https instead of http</p>
</div>
<div id="comment-59571-info" class="comment-info">
<span class="comment-age">(12 Sep '17, 16:55)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="66138"></span>
<div id="comment-66138" class="comment">
<div id="post-66138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also first noticed this error in Chrome, and wrote a blog post about it here: <a href="http://harrywood.co.uk/blog/2016/07/21/leaflet-geolocation-error/">http://harrywood.co.uk/blog/2016/07/21/leaflet-geolocation-error/</a> but I see nowadays firefox and safari have followed, locking it down so you can only geolocate if you're on a secure connection.</p>
</div>
<div id="comment-66138-info" class="comment-info">
<span class="comment-age">(02 Oct '18, 23:31)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-59570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59570-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59572"></span>

<div id="answer-container-59572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59572-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-59572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two issues here:</p>
<p>One is the display that you see when you first open the OSM website. In a new window with no cookies etc., I get a map of Western Europe; I think that this is either based on IP address geolocation or just the default - see <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1586#issuecomment-315515644">here</a> for an explanation of that.</p>
<p>The other issue is what happens when you click the "show my location" button. That has the web site ask your web browser where it thinks it is. As the <a href="https://www.chromium.org/Home/chromium-security/prefer-secure-origins-for-powerful-new-features">link</a> indicates, recent versions of Chrome and Chromium won't send your location to a website unless it's over an https connection. Also <a href="https://www.clickssl.net/blog/geolocation-with-firefox-55-https-will-require">Firefox 55+</a>. There's an issue for this one <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1493">here</a>, and the decision to not send your location to OSM is your browser's, not OSM's.</p>
<p>There's been discussion about whether it's a good idea for OSM to <em>only</em> support https, and there are arguments both for and against that that have been discussed ad nauseum in github and on mailing lists etc.</p>
<p>As nevw has said, if you browse to <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> the "show my location button" will work, which will probably result in another prompt from your browser asking whether you want to share your location with OpenStreetMap.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '17, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '17, 18:03</strong> </span></p>
</div>
</div>
<div id="comments-container-59572" class="comments-container">
<span id="59573"></span>
<div id="comment-59573" class="comment">
<div id="post-59573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thank you both for your responses. I have opened OSM using the link above. Clicking 'Show my location' resulted in Geolocation error: Network location provider at 'https://www.googleapis.com/' : Returned error code 403.. this time, so still no success, unfortunately. Typing 'Binfield Heath' into the search bar gets me to where I need to be very quickly, so I might find the situation resolves itself as unexpectedly as it appeared a few days ago. I have no such issue on my Android 'phone, using the same browser and search engine.</p>
</div>
<div id="comment-59573-info" class="comment-info">
<span class="comment-age">(12 Sep '17, 20:50)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
</div>
<div id="comment-tools-59572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59572-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62881"></span>

<div id="answer-container-62881" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62881-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had this error message and followed the explanatory link, which was mostly incomprehensible to an "ordinary" user of OSM. Such gems as "a service worker script that had been tampered with because they got it over a MITM’d or spoofed cafe wifi connection" are all well and good, but it would have been more useful to put, simply, "Check you are using https" or something similar. KISS :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '18, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/b08048ac9d44d00ef10cb867579a2fcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xxxxxxxxxxxxxx&#39;s gravatar image" />
<p><span>xxxxxxxxxxxxxx</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xxxxxxxxxxxxxx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62881" class="comments-container">
<span id="62882"></span>
<div id="comment-62882" class="comment">
<div id="post-62882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The page you're refering to is part of <a href="https://sites.google.com/a/chromium.org/dev/Home/chromium-security/prefer-secure-origins-for-powerful-new-features">Chrome's documentation</a>. It is an open source project so in theory you could contribute to making that page more helpful, though I'm not sure which part of "recent versions of Chrome and Chromium won't send your location to a website unless it's over an https connection" was unclear :)</p>
</div>
<div id="comment-62882-info" class="comment-info">
<span class="comment-age">(01 Apr '18, 10:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62881-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


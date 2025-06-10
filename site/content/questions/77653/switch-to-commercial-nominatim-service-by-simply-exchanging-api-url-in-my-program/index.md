+++
type = "question"
title = "Switch to commercial nominatim service by simply exchanging api-URL in my program..."
description = '''Hello OSM-Team,  thank you for your great service - it&#x27;s awesome! I have a seemingly easy task, which I couldn&#x27;t solve by simple research. I have an existing application running in test mode using your nominatim API. So far so good and working fine. I would like to find a higher volume service which...'''
date = "2020-11-21T15:46:00Z"
lastmod = "2021-08-01T13:46:00Z"
weight = 77653
keywords = [ "switch", "nominatim", "provider" ]
aliases = [ "/questions/77653" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Switch to commercial nominatim service by simply exchanging api-URL in my program...](/questions/77653/switch-to-commercial-nominatim-service-by-simply-exchanging-api-url-in-my-program)

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
<span id="post-77653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77653-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSM-Team, thank you for your great service - it's awesome! I have a seemingly easy task, which I couldn't solve by simple research. I have an existing application running in test mode using your nominatim API. So far so good and working fine.</p>
<p>I would like to find a higher volume service which allows several requests per second (paid for no problem) by just exchanging the api-URL in my program code and no other changes whatsoever. Exchange URL -&gt; Program works as before.</p>
<p>I.e.: "https://nominatim.openstreetmap.org/" exchanged by "https://nominatimxyz.newOSMservice.com/" will keep my system running - just with higher volume usage possibilities.</p>
<p>I have checked your list of alternatives but haven't found guidance on that topic so far. Do you know any service which works the EXACT same way for requests which could allow me to proceed as described above? (I know I could use my own server installation, which seems a bit early and time consuming so far - unless there would be ready made installation packages for AWS or the like). If you had a hint where I can start digging without contacting all alternative providers - would be great.</p>
<p>Many thanks in advance for any suggestions or guidance and kind regards!</p>
<p>Markus</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-provider" rel="tag" title="see questions tagged &#39;provider&#39;">provider</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '20, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ac580142502ab52e37e7fea3b3961389?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfschueler&#39;s gravatar image" />
<p><span>mfschueler</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfschueler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77653" class="comments-container">
&#10;</div>
<div id="comment-tools-77653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77653-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="77654"></span>

<div id="answer-container-77654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77654-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>LocationIQ (<a href="https://www.locationiq.com"></a><a href="https://www.locationiq.com">https://www.locationiq.com</a>), Forward &amp; Reverse Geocoding @ RapidAPI (<a href="https://rapidapi.com/GeocodeSupport/api/forward-reverse-geocoding">https://rapidapi.com/GeocodeSupport/api/forward-reverse-geocoding</a>) or Geofabrik (<a href="https://www.geofabrik.de"></a><a href="https://www.geofabrik.de">https://www.geofabrik.de</a>) should all offer this without a problem.</p>
<p>You just change the Nominatim url to an url by the provider and add an apikey query param - or send that last one as an extra header.</p>
<p>(Note: the following urls won't work without an apikey)</p>
<p>E.g. <a href="https://us1.locationiq.com/v1/search.php?key=YOURACCESSTOKEN&amp;q=SEARCHSTRING&amp;format=json">https://us1.locationiq.com/v1/search.php?key=YOURACCESSTOKEN&amp;q=SEARCHSTRING&amp;format=json</a></p>
<p>or</p>
<p><a href="https://forward-reverse-geocoding.p.rapidapi.com/v1/search?rapidapi-key=YOURACCESSTOKEN&amp;q=SEARCHSTRING&amp;format=json">https://forward-reverse-geocoding.p.rapidapi.com/v1/search?rapidapi-key=YOURACCESSTOKEN&amp;q=SEARCHSTRING&amp;format=json</a></p>
<p>For Reverse Geocoding it would be:</p>
<p><a href="https://us1.locationiq.com/v1/reverse.php?key=YOURACCESSTOKEN&amp;lat=LATITUDE&amp;lon=LONGITUDE&amp;format=json">https://us1.locationiq.com/v1/reverse.php?key=YOURACCESSTOKEN&amp;lat=LATITUDE&amp;lon=LONGITUDE&amp;format=json</a></p>
<p>or</p>
<p><a href="https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse?rapidapi-key=YOURACCESSTOKEN&amp;lat=LATITUDE&amp;lon=LONGITUDE&amp;format=json">https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse?rapidapi-key=YOURACCESSTOKEN&amp;lat=LATITUDE&amp;lon=LONGITUDE&amp;format=json</a></p>
<p>(I don't know about the URLs of Geofabrik, you would have to ask them).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '20, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '20, 16:29</strong> </span></p>
</div>
</div>
<div id="comments-container-77654" class="comments-container">
<span id="77655"></span>
<div id="comment-77655" class="comment">
<div id="post-77655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow - many thanks already for quick high quality help! Kind regards!</p>
</div>
<div id="comment-77655-info" class="comment-info">
<span class="comment-age">(21 Nov '20, 16:41)</span> <span class="comment-user userinfo">mfschueler</span>
</div>
</div>
</div>
<div id="comment-tools-77654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77656"></span>

<div id="answer-container-77656" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77656-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Ed here from <a href="https://opencagedata.com/">OpenCage</a> here. We offer a geocoding API based on open data including (but not only) OSM. Behind the scenes we use nominatim and many others (we also sponsor the development of nominatim, and are silver tier corporate members of the OSMF). We would love to work with you, as we do with many others. That said, we don't offer one to one URL replacement of the type it seems you want, mainly because we do a bit more than just nominatim. <a href="https://opencagedata.com/sdks">We have SDKs for 30+ programming languages</a>, so I imagine a switch would not be particularly difficult. Though I say that without knowing your use case. Happy to chat if you think it useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '20, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/696d78192310159e012d83e6c377d257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdFreyfogle&#39;s gravatar image" />
<p><span>EdFreyfogle</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdFreyfogle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77656" class="comments-container">
<span id="77658"></span>
<div id="comment-77658" class="comment">
<div id="post-77658-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Ed, thank you for the information. For now I have to stay as lean as possible - like described above. Kind regards!</p>
</div>
<div id="comment-77658-info" class="comment-info">
<span class="comment-age">(22 Nov '20, 08:53)</span> <span class="comment-user userinfo">mfschueler</span>
</div>
</div>
</div>
<div id="comment-tools-77656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77656-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81157"></span>

<div id="answer-container-81157" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We provide geocoding api for forward and reverse geocoding. We are able to provide high volume with reduced prices contact us at support@geokeo.com if you require more information. Our service is available at <a href="https://geokeo.com">Geokeo</a> and our documentation is located at <a href="https://geokeo.com/documentation.php">Geokeo Documentation</a>. give it a try at our demo page where you can try our services without registration or api key - <a href="https://geokeo.com/demo.php">Geokeo Demo</a>. Thank you Geokeo Team</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '21, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/013be43a63d8f8be0f9ab27d6e48ca4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="duttaarc&#39;s gravatar image" />
<p><span>duttaarc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="duttaarc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81157" class="comments-container">
&#10;</div>
<div id="comment-tools-81157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81157-form-container" class="comment-form-container">
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


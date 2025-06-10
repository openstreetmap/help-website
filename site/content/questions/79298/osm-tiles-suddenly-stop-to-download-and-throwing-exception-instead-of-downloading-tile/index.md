+++
type = "question"
title = "OSM tiles suddenly stop to download and throwing exception instead of downloading tile"
description = '''Hi All, I am using OSM maps in my application and download tiles from tile https://tile.openstreetmap.org/. I am using WebClient to download the tile from OSM server. It is worked perfectly before 5 days. But suddenly, tiles not downloaded from server and maps not displayed in my application. I used...'''
date = "2021-03-16T14:59:00Z"
lastmod = "2021-03-17T14:17:00Z"
weight = 79298
keywords = [ "openstreetmap", "xamarin", "c#", "osm", "android" ]
aliases = [ "/questions/79298" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM tiles suddenly stop to download and throwing exception instead of downloading tile](/questions/79298/osm-tiles-suddenly-stop-to-download-and-throwing-exception-instead-of-downloading-tile)

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
<span id="post-79298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I am using OSM maps in my application and download tiles from tile <a href="https://tile.openstreetmap.org/.">https://tile.openstreetmap.org/.</a> I am using WebClient to download the tile from OSM server. It is worked perfectly before 5 days. But suddenly, tiles not downloaded from server and maps not displayed in my application. I used below code to download tile.</p>
<p>imageBytes = await webClient.DownloadDataTaskAsync(imageUri);</p>
<p>I have checked the source and getting the below exception in try catch.</p>
<p><strong>The remote server returned an error: (403) Forbidden.</strong></p>
<p>To resolve this, i set the below properties as true but still maps not displayed in my application.</p>
<p>webClient.UseDefaultCredentials = true; webClient.Proxy.Credentials = System.Net.CredentialCache.DefaultCredentials;</p>
<p>Any one please help me to resolve this issue.</p>
<p>Regards, Bharathi.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xamarin" rel="tag" title="see questions tagged &#39;xamarin&#39;">xamarin</span> <span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '21, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b63c0f7bf24c1e2ef9e1755baa927e18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bharathirajak&#39;s gravatar image" />
<p><span>Bharathirajak</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bharathirajak has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79298" class="comments-container">
<span id="79299"></span>
<div id="comment-79299" class="comment">
<div id="post-79299-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you estimate how many tiles you have downloaded in this way?</p>
</div>
<div id="comment-79299-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 15:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="79300"></span>
<div id="comment-79300" class="comment">
<div id="post-79300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is not working for first level itself. It has just 4 tiles</p>
</div>
<div id="comment-79300-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 15:41)</span> <span class="comment-user userinfo">Bharathirajak</span>
</div>
</div>
<span id="79301"></span>
<div id="comment-79301" class="comment">
<div id="post-79301-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But you said it worked 5 days ago. How many tiles have you downloaded in this way in the last couple of months until it stopped working?</p>
</div>
<div id="comment-79301-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 16:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="79304"></span>
<div id="comment-79304" class="comment">
<div id="post-79304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the problem is not related to downloading more tiles. Because the issue can be reproduced in simple sample itself by using the above code to download tiles. I have tested with simple sample and different machine and devices.</p>
</div>
<div id="comment-79304-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 17:12)</span> <span class="comment-user userinfo">Bharathirajak</span>
</div>
</div>
<span id="79308"></span>
<div id="comment-79308" class="comment">
<div id="post-79308-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This issue particularly reproduced when using web client in Xamarin.Forms Android and iOS. In Forms.UWP, we directly used url to image source and it is working fine.</p>
</div>
<div id="comment-79308-info" class="comment-info">
<span class="comment-age">(17 Mar '21, 07:51)</span> <span class="comment-user userinfo">Bharathirajak</span>
</div>
</div>
</div>
<div id="comment-tools-79298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79298-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="79309"></span>

<div id="answer-container-79309" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79309-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-79309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bharathirajak has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are probably not following the tile usage policy found here: <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
<p>Esp. you'll need a User-Agent that is not generic but specific to your application and also adhere to the other Technical Usage Requirements (see policy document). You'll also have to follow the bulk downloading restrictions (not loading more than 250 tiles from zoom 13 or grater).</p>
<p>Best idea would be to use one of external tile providers if it is for a commercial application that needs reliability or - if that's not the case - try to follow the technical requirements from the usage policy. And Frederiks question is still valid: how many tiles has your app loaded already? If those numbers are too high, you may get blocked as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '21, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79309" class="comments-container">
<span id="79310"></span>
<div id="comment-79310" class="comment">
<div id="post-79310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Spiekerooger,</p>
<p>Thanks for your update. But, it is reproduced in simple sample. Just downloaded a single tile statically in this. Please find the sample link.<br />
<a href="https://github.com/bharathirajauk/MySamples/blob/master/Maps.zip">https://github.com/bharathirajauk/MySamples/blob/master/Maps.zip</a></p>
</div>
<div id="comment-79310-info" class="comment-info">
<span class="comment-age">(17 Mar '21, 11:19)</span> <span class="comment-user userinfo">Bharathirajak</span>
</div>
</div>
<span id="79311"></span>
<div id="comment-79311" class="comment">
<div id="post-79311-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Sorry, but you did not answer any of the questions above. Again: your application got blocked in accessing tiles because it does not follow the tile usage policy. That's why you get a http 403 error. So: do you use a unique user-agent string? How many tile requests do you send on average and how many tile requests did you sent already?</p>
<p>And looking at your code: you are faking a generic user-agent. In doing so, you get blocked.</p>
</div>
<div id="comment-79311-info" class="comment-info">
<span class="comment-age">(17 Mar '21, 11:29)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="79316"></span>
<div id="comment-79316" class="comment">
<div id="post-79316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer and confirm the problem is related to User-Agent that is not generic. I have created Xamarin mobile app to show the OSM map. I will request tile server for each pinch zooming on map based on the zooming level. I don’t know exactly how many requests given already; it is depending on application testing usage. Can you please let me know how to pass valid and generic user agent? it's related to the OSM usage policy.?</p>
</div>
<div id="comment-79316-info" class="comment-info">
<span class="comment-age">(17 Mar '21, 14:17)</span> <span class="comment-user userinfo">Bharathirajak</span>
</div>
</div>
</div>
<div id="comment-tools-79309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79309-form-container" class="comment-form-container">
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


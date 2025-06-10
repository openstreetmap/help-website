+++
type = "question"
title = "Upload Objects from own Android OSM App"
description = '''Dear OSM Community, i&#x27;m developing my own little Android application (Android Studio). In that app i would like to implement an &quot;add new OSM objects&quot; function e.g. adding nodes, ways or areas and furthermore upload these objects from my app to OSM Server. is it possible at all to upload some data fr...'''
date = "2016-11-10T22:12:00Z"
lastmod = "2016-11-12T13:13:00Z"
weight = 52886
keywords = [ "development", "android", "objects", "nodes", "upload" ]
aliases = [ "/questions/52886" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Upload Objects from own Android OSM App](/questions/52886/upload-objects-from-own-android-osm-app)

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
<span id="post-52886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM Community,</p>
<p>i'm developing my own little Android application (Android Studio). In that app i would like to implement an "add new OSM objects" function e.g. adding nodes, ways or areas and furthermore upload these objects from my app to OSM Server. is it possible at all to upload some data from own developed Android application to OSM server? Do I need any permissions for that? Do you have some suggestions for me for the implementation or some useful links? I downloaded and took a look at the open source code of the Vespucci App but that code is really big and complicated.</p>
<p>Best Felix</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '16, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/fa8b7093d320cfac4f28a2b1bafea619?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChelseaChels&#39;s gravatar image" />
<p><span>ChelseaChels</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChelseaChels has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '16, 11:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52886" class="comments-container">
&#10;</div>
<div id="comment-tools-52886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52886-form-container" class="comment-form-container">
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

<span id="52888"></span>

<div id="answer-container-52888" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52888-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ChelseaChels has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are multiple points to consider, among others:</p>
<ul>
<li>You naturally can upload new and edited elements via <a href="https://wiki.openstreetmap.org/wiki/API">the Editing API</a>, that is what it is there for. You need an OSM account to write data, there is no special authorization required beyond that.</li>
<li>it is good practice, not to say a requirement, that you provide a facility that allows the user to determine if the object they believe is missing is actually not already mapped, this includes all possible ways the object in question can be created in OSM</li>
<li>any testing needs to done against the dev sandboxes see <a href="http://apis.dev.openstreetmap.org/">http://apis.dev.openstreetmap.org/</a></li>
</ul>
<p>If your app starts breaking stuff you will be burnt to a crisp (but that has happened to the best of us).</p>
<p>Further you probably should have a quick look at <a href="http://2016.stateofthemap.org/2016/staying-on-the-right-side-best-practices-in-editing/">my talk at SOTM 2016 on the topic</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '16, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '16, 08:00</strong> </span></p>
</div>
</div>
<div id="comments-container-52888" class="comments-container">
<span id="52897"></span>
<div id="comment-52897" class="comment">
<div id="post-52897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks SimonPoole, that is what i'm talking about!</p>
</div>
<div id="comment-52897-info" class="comment-info">
<span class="comment-age">(12 Nov '16, 13:13)</span> <span class="comment-user userinfo">ChelseaChels</span>
</div>
</div>
</div>
<div id="comment-tools-52888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52888-form-container" class="comment-form-container">
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


+++
type = "question"
title = "thunderforest api key in QGIS 3"
description = '''I know this has been beaten to death, but I don&#x27;t see how to do this in QGIS 3. I have the API Key and Tile Layer URL. So I add OSM Cycle Map via Web&amp;gt;Quick Map Services&amp;gt;OSM I right click on Properties in Layers, but then what do I do? Here&#x27;s the screen shot on macOS, QGIS 3.2.3 Thanks'''
date = "2018-10-20T22:44:00Z"
lastmod = "2018-12-14T13:54:00Z"
weight = 66403
keywords = [ "qgis", "qgis_3", "opencyclemap" ]
aliases = [ "/questions/66403" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [thunderforest api key in QGIS 3](/questions/66403/thunderforest-api-key-in-qgis-3)

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
<span id="post-66403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66403-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know this has been <a href="/questions/55965/thunderforest-api-key-and-qgis">beaten to death</a>, but I don't see how to do this in QGIS 3.</p>
<p>I have the API Key and Tile Layer URL.</p>
<p>So I add OSM Cycle Map via Web&gt;Quick Map Services&gt;OSM</p>
<p>I right click on Properties in Layers, but then what do I do? Here's the screen shot on macOS, QGIS 3.2.3<img src="/upfiles/OSM_properties_AI3zpLy.png" alt="alt text" /></p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-qgis_3" rel="tag" title="see questions tagged &#39;qgis_3&#39;">qgis_3</span> <span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '18, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/262ace94f9a2925629114f9260378be5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MtnBiker&#39;s gravatar image" />
<p><span>MtnBiker</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MtnBiker has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '18, 23:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66403" class="comments-container">
&#10;</div>
<div id="comment-tools-66403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66403-form-container" class="comment-form-container">
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

<span id="67193"></span>

<div id="answer-container-67193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67193-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-67193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I also struggled a couple of hours to enter the API Key of Thunderforest in QGIS3.</p>
<p>The OSM layer must not be added via QuickMapService.</p>
<p>Instead, in the browser, there is an entry "XYZ tiles"</p>
<p>Right click, "new connection"</p>
<p>in Name: write whatever you want. "OSM Landscape Map " is quite good.</p>
<p>in URL: write the "https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=xxxxx" (put your API Key) click OK</p>
<p>A new entry 'OSM Landscape' appears under XYZ tiles</p>
<p>Right click it, "Add selected leyers to canvas".</p>
<p>Done !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '18, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e4b70ab7adc92cad2e55bad6781ba316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ospeleo&#39;s gravatar image" />
<p><span>ospeleo</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ospeleo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '18, 13:02</strong> </span></p>
</div>
</div>
<div id="comments-container-67193" class="comments-container">
<span id="67195"></span>
<div id="comment-67195" class="comment">
<div id="post-67195-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16045/ospeleo">@ospeleo</a>: useful, XYZ tiles are non-obvious if one is used to earlier versions of QGIS.</p>
</div>
<div id="comment-67195-info" class="comment-info">
<span class="comment-age">(14 Dec '18, 13:54)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67193-form-container" class="comment-form-container">
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


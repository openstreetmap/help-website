+++
type = "question"
title = "How to import indoor mapping .osm files in Vespucci?"
description = '''Hi, I&#x27;m totally new to OSM, and I&#x27;m trying to figure out how to map a train station. Regarding the mapping process, the transport operator I work for can provide me station maps which shows only the main walls of a floor, I thought about using it as a layer in Vespucci and go on site and edit POI an...'''
date = "2015-05-27T17:51:00Z"
lastmod = "2020-06-10T06:22:00Z"
weight = 43264
keywords = [ "indoor", "josm", "editing", "vespucci", "import" ]
aliases = [ "/questions/43264" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to import indoor mapping .osm files in Vespucci?](/questions/43264/how-to-import-indoor-mapping-osm-files-in-vespucci)

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
<span id="post-43264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43264-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm totally new to OSM, and I'm trying to figure out how to map a train station. Regarding the mapping process, the transport operator I work for can provide me station maps which shows only the main walls of a floor, I thought about using it as a layer in Vespucci and go on site and edit POI and other stuff using a Lenovo Yoga Tablet 2 on Android.</p>
<p>As I wanted to test this workflow, I tried to load an ".osm" sample I found in the french OSM wiki: <a href="http://line2soft.monespace.net/ftp/Exemple.osm">http://line2soft.monespace.net/ftp/Exemple.osm</a></p>
<p>I can open this file in JOSM, but it is not possible to load it in Vespucci using "Transfer"-&gt; "Read from a file". After the import, nothing happens, I'm a just stuck with the world map.</p>
<p>What's wrong with my import?<br />
Or is there another indoor mapping process which could be a good workaround?</p>
<p>Thanks for your help.</p>
<p>Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-vespucci" rel="tag" title="see questions tagged &#39;vespucci&#39;">vespucci</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '15, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e14e57f46475fe84cbe732ea404a2d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haristide&#39;s gravatar image" />
<p><span>Haristide</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haristide has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '15, 17:53</strong> </span></p>
</div>
</div>
<div id="comments-container-43264" class="comments-container">
&#10;</div>
<div id="comment-tools-43264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43264-form-container" class="comment-form-container">
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

<span id="52831"></span>

<div id="answer-container-52831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52831-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This actually a bug report (not sure why it is turning up now given that it is from May 2015), you should open an issue here: <a href="https://github.com/MarcusWolschon/osmeditor4android/issues">https://github.com/MarcusWolschon/osmeditor4android/issues</a> it seems however as if the sample file is no longer available.</p>
<p>BTW the next release of vespucci will have an "indoor" mode, a beta of this is likely 1-2 weeks away (see <a href="https://twitter.com/sp8962/status/791398313669103616">https://twitter.com/sp8962/status/791398313669103616</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '16, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-52831" class="comments-container">
&#10;</div>
<div id="comment-tools-52831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52831-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75262"></span>

<div id="answer-container-75262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75262-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-75262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To add OSM data using Vespucci, you are required to sign in to your OpenStreetMap account. Sign in by tapping the “More options” icon (located on the lower right portion of the screen) and selecting “Authorise OAuth” under “Tools…”. Type your OSM username (or email address) and password, then tap “Login”. If you do not have an OSM account, select “Register now” instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '20, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75262" class="comments-container">
&#10;</div>
<div id="comment-tools-75262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75262-form-container" class="comment-form-container">
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


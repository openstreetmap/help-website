+++
type = "question"
title = "Problem: Potlatch2 doesn&#x27;t save the changes (Despite of correct log-in)"
description = '''Hi everybody! I&#x27;m new to OSM / Potlatch2. After studying tutorials, I pretty customized my Potlatch2 with correct configuration (at least it appears to be so, I can connect / log-in / read data etc). My aim is to create a custom map of accessibility for disabled people with own signatures and attrib...'''
date = "2012-04-19T10:48:00Z"
lastmod = "2012-04-20T12:46:00Z"
weight = 12167
keywords = [ "attributes", "changeset", "schema", "creating", "error" ]
aliases = [ "/questions/12167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem: Potlatch2 doesn't save the changes (Despite of correct log-in)](/questions/12167/problem-potlatch2-doesnt-save-the-changes-despite-of-correct-log-in)

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
<span id="post-12167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12167-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody!</p>
<p>I'm new to OSM / Potlatch2. After studying tutorials, I pretty customized my Potlatch2 with correct configuration (at least it appears to be so, I can connect / log-in / read data etc).</p>
<p>My aim is to create a custom map of accessibility for disabled people with own signatures and attributes (based on munitipal data which was offered fot this aim). The symbology (pictogramms) and attributes implemented in XML files seems to work well.</p>
<p>But after clicking on "Save changes" an error alert appears: "Error creating changeset".</p>
<p>First, I thought that the failure origins in the change of OSM-Schema. (By the way, may I create my own attributes and write them back to OSM?) I changed everything back / installed the "original" potlatch2 and tried to complete the standard OSM with standard OSM-own attributes. And it doesn't work either - the same error alert appears again.</p>
<p>Does anyone know what the cause for that error can be? May I use and write to OMS additional features/symbology/attributes?</p>
<p>Thank you in advance Geo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span> <span class="post-tag tag-link-creating" rel="tag" title="see questions tagged &#39;creating&#39;">creating</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '12, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/66b6c0e7b3244335574f8e74765e514b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoSingularity&#39;s gravatar image" />
<p><span>GeoSingularity</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoSingularity has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12167" class="comments-container">
<span id="12173"></span>
<div id="comment-12173" class="comment">
<div id="post-12173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to confirm - you've deployed your own copy of Potlatch2 on your own server and it's there that you're getting problems with save?</p>
</div>
<div id="comment-12173-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 12:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12167-form-container" class="comment-form-container">
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

<span id="12170"></span>

<div id="answer-container-12170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12170-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-12170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's very possibly an OAuth error, I think. Have you followed the <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Deploying_Potlatch_2">instructions on the wiki</a> to get the 'consumer key' and 'consumer secret' correct?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '12, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-12170" class="comments-container">
<span id="12171"></span>
<div id="comment-12171" class="comment">
<div id="post-12171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, yes, I followed the instructions and got the keys already several times from different servers - without success.</p>
<p>I also changed the paths (as described in the instruction from api06.dev to www.</p>
<p>One thing I left is the Server Name: args["serverName"] = "api06 Test On Dev"</p>
<p>Should it be also changed? If yes, how is the main OSM server properly called?</p>
</div>
<div id="comment-12171-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 12:18)</span> <span class="comment-user userinfo">GeoSingularity</span>
</div>
</div>
<span id="12196"></span>
<div id="comment-12196" class="comment">
<div id="post-12196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, the server name shouldn't make any difference.</p>
<p>If your P2 instance is publicly accessible (or you can upload it somewhere), then post the URL here and we can take a look - it's difficult to debug remotely otherwise.</p>
</div>
<div id="comment-12196-info" class="comment-info">
<span class="comment-age">(20 Apr '12, 12:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12170-form-container" class="comment-form-container">
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


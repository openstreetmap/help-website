+++
type = "question"
title = "Error in JOSM preset prolog"
description = '''Below is a JOSM preset I&#x27;m developing that generates an error. I&#x27;m new to XML and cannot see the error and wonder if anyone else can. JOSM reports the following error when I try to add the code as a Custom Preset in JOSM v. 7182. Error is [1:1] Content is not allowed in prolog. (note: I replaced all...'''
date = "2014-06-03T22:01:00Z"
lastmod = "2014-06-05T08:03:00Z"
weight = 33651
keywords = [ "josm", "presets" ]
aliases = [ "/questions/33651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error in JOSM preset prolog](/questions/33651/error-in-josm-preset-prolog)

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
<span id="post-33651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Below is a JOSM preset I'm developing that generates an error. I'm new to XML and cannot see the error and wonder if anyone else can. JOSM reports the following error when I try to add the code as a Custom Preset in JOSM v. 7182.</p>
<p><strong>Error is [1:1]<br />
Content is not allowed in prolog.</strong></p>
<p>(note: I replaced all "&lt;" with "{" and all "&gt;" with "}" so the code below will display properly)</p>
<p>{presets xmlns="http://josm.openstreetmap.de/tagging-preset-1.0"}<br />
{item name="Tennis court" type="way,closedway"}<br />
{label text="Tagging a tennis court" /}<br />
{key key="leisure" value="pitch" /}<br />
{key key="sport" value="tennis" /}<br />
{check key="fee" text="Fee: " default="off" delete_if_empty="true" /}<br />
{check key="lit" text="Lit: " default="off" delete_if_empty="true" /}<br />
{check key="access" text="Access (yes)" default="on" delete_if_empty="true" /}<br />
{check key="name" text="Name Here " default=" " delete_if_empty="true" /}<br />
{key key="source" value="Bing" /}<br />
{key key="source:name" value="Internet" /}<br />
{key key="surface" value="asphalt" /}<br />
{/item}<br />
{/presets}</p>
<p>Thanks very much...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-presets" rel="tag" title="see questions tagged &#39;presets&#39;">presets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '14, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33651" class="comments-container">
<span id="33661"></span>
<div id="comment-33661" class="comment">
<div id="post-33661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note enclosing code in back ticks will stop it from being interpreted as HTML.</p>
</div>
<div id="comment-33661-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 08:40)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33651-form-container" class="comment-form-container">
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

<span id="33677"></span>

<div id="answer-container-33677" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33677-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is that you have</p>
<p>check key="name" text="Name Here " default=" " delete_if_empty="true"</p>
<p>you probably meant to have key here. Check is a checkbox. That cannot have an empty default. replace check with key and it work (at least for me)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '14, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33677" class="comments-container">
<span id="33679"></span>
<div id="comment-33679" class="comment">
<div id="post-33679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are quite right escada. I changed that line to<br />
key key="name" text="Name Here " default=" " delete_if_empty="true"<br />
however, it still produces the same error. You said you loaded it and it worked for you. Would you please post your exact version here?</p>
</div>
<div id="comment-33679-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 17:44)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="33685"></span>
<div id="comment-33685" class="comment">
<div id="post-33685-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, my bad, it has to be "text key="name" text="Name Here " default=" " delete_if_empty="true"</p>
</div>
<div id="comment-33685-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 20:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33692"></span>
<div id="comment-33692" class="comment">
<div id="post-33692-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, that's not it either. Still the same error. Wouldn't it be nice if such error messages would be more explanatory. The days of computers with limited space for text storage are long gone. Y2K is 14 years behind us!</p>
</div>
<div id="comment-33692-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 23:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="33694"></span>
<div id="comment-33694" class="comment">
<div id="post-33694-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Is there any character before the first "&lt;" ? A white space, a blank line ? "Content not allowed in prolog" means there is content, aka characters before the first accepted character, which has to be a "&lt;</p>
<p>I'm stil struggling to get the content of the file that is working back to you. Is this dropbox link working for you <a href="https://db.tt/Ub8ziKFr">https://db.tt/Ub8ziKFr</a></p>
</div>
<div id="comment-33694-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 04:21)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33695"></span>
<div id="comment-33695" class="comment">
<div id="post-33695-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Finally! Got it. Yes, there was some spurious data in front of the leading "&lt;". Where it came from is beyond me. I only found it by comparing your XML file and mine with ExamDiff, an old friend of mine.</p>
<p>Thanks so much for your help escada.</p>
</div>
<div id="comment-33695-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 06:47)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="33697"></span>
<div id="comment-33697" class="comment not_top_scorer">
<div id="post-33697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you're welcome. Glad I could help</p>
</div>
<div id="comment-33697-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 08:03)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-33677" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33677-form-container" class="comment-form-container">
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


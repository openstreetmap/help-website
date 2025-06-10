+++
type = "question"
title = "How do I specify a preferences.xml file when I invoke JOSM ?"
description = '''Hello ! I would like to config JOSM for two different uses but with the same user. I find a preference file here : ~/.josm/preferences.xml and he seems that I can define the var JOSM_ARGS when I invoke josm-tested.jar but I don&#x27;t find any documentation about it. Is there a method like that JOSM_ARGS...'''
date = "2016-02-18T07:55:00Z"
lastmod = "2016-02-18T08:41:00Z"
weight = 48197
keywords = [ "josm", "preference", "arguments" ]
aliases = [ "/questions/48197" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I specify a preferences.xml file when I invoke JOSM ?](/questions/48197/how-do-i-specify-a-preferencesxml-file-when-i-invoke-josm)

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
<span id="post-48197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48197-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello ! I would like to config JOSM for two different uses but with the same user. I find a preference file here : <code>~/.josm/preferences.xml</code> and he seems that I can define the var <code>JOSM_ARGS</code> when I invoke josm-tested.jar but I don't find any documentation about it.</p>
<p>Is there a method like that <code>JOSM_ARGS="-f ~/.josm/other_preferences_file.xml"</code></p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-preference" rel="tag" title="see questions tagged &#39;preference&#39;">preference</span> <span class="post-tag tag-link-arguments" rel="tag" title="see questions tagged &#39;arguments&#39;">arguments</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '16, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/828965e22971cea0ec879d070c515968?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lhapaipai&#39;s gravatar image" />
<p><span>lhapaipai</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lhapaipai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48197" class="comments-container">
&#10;</div>
<div id="comment-tools-48197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48197-form-container" class="comment-form-container">
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

<span id="48198"></span>

<div id="answer-container-48198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48198-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to suggest you can <a href="https://josm.openstreetmap.de/wiki/Help/CommandLineOptions">here</a><br />
--load-preferences=&lt;url-to-xml&gt; Changes preferences according to the XML file</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '16, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
</div>
<div id="comments-container-48198" class="comments-container">
<span id="48199"></span>
<div id="comment-48199" class="comment">
<div id="post-48199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you !</p>
</div>
<div id="comment-48199-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 08:41)</span> <span class="comment-user userinfo">lhapaipai</span>
</div>
</div>
</div>
<div id="comment-tools-48198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48198-form-container" class="comment-form-container">
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


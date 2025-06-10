+++
type = "question"
title = "why are my HOT auto-generated edit sumeries so badly formated?"
description = '''I&#x27;ve been editing HOT tasks, using JOSM. It auto generates an edit summary for me, but mine is full of the type of markup that is used in URLs to encode less common characters. Like &quot;%23&quot; instead of &quot;#&quot;. It leaves my edit summaries almost unreadable. Is this a known issue? Any known workarounds? I d...'''
date = "2015-04-29T21:17:00Z"
lastmod = "2015-04-29T21:25:00Z"
weight = 42709
keywords = [ "josm", "hot", "nepal", "changeset_comment" ]
aliases = [ "/questions/42709" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why are my HOT auto-generated edit sumeries so badly formated?](/questions/42709/why-are-my-hot-auto-generated-edit-sumeries-so-badly-formated)

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
<span id="post-42709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42709-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been editing HOT tasks, using JOSM. It auto generates an edit summary for me, but mine is full of the type of markup that is used in URLs to encode less common characters. Like "%23" instead of "#". It leaves my edit summaries almost unreadable. Is this a known issue? Any known workarounds? I don't see any obvious links on the HOT website to submit bug reports.</p>
<p>I'm viewing the HOT website on firefox, my computer is running Ubuntu 14.10, and the most up to date version of JOSM (Version 8279).</p>
<p><strong>edit:</strong> <a href="http://www.openstreetmap.org/changeset/30633750">example</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-hot" rel="tag" title="see questions tagged &#39;hot&#39;">hot</span> <span class="post-tag tag-link-nepal" rel="tag" title="see questions tagged &#39;nepal&#39;">nepal</span> <span class="post-tag tag-link-changeset_comment" rel="tag" title="see questions tagged &#39;changeset_comment&#39;">changeset_comment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '15, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '15, 22:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42709" class="comments-container">
&#10;</div>
<div id="comment-tools-42709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42709-form-container" class="comment-form-container">
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

<span id="42711"></span>

<div id="answer-container-42711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42711-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you see is a <span>URL encoded</span> text.</p>
<p>workaround: just fix your edit summaries manually before you upload.</p>
<p>investigation (assuming that HOT uses JOSM's remote control which is backed by the ticket/issues linked further down): <a href="https://127.0.0.1:8112/load_and_zoom?left=8.19&amp;right=8.20&amp;top=48.605&amp;bottom=48.590&amp;select=node413602999&amp;changeset_comment=%23hashtag%20-%20this%20is%20a%20test%20comment">HTTPS test link with a preset changeset comment</a> works for me with version 8291 and with version 8279 (with the older 8109 I get no pre-filled comment at all, whyever): I see "#hashtag - this is a test comment" in the comment box (after doing a simple node move and clicking the upload button). Note: please do not really upload such test data, do not click the final upload button! (technical note: yes, a non-encoded # seems to be not liked by JOSM – see #issuecomment-75121152 in the "issue" mentioned further down)</p>
<p>So, it seems to me that the HOT website constructs the Remote Control link somehow wrong (too much encoding). <del>Please tell the HOT guys (also tell them your JOSM version). See <a href="https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team#Contact_and_Media_Resources">https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team#Contact_and_Media_Resources</a> for contact options.</del> I have written user pyrog a mail and further communication is best made in the relevant "issue" at github (see below).</p>
<p>Further note: this seems to be known as <a href="https://josm.openstreetmap.de/ticket/10975">https://josm.openstreetmap.de/ticket/10975</a> ("JOSM's behaviour is correct for the given request" and "Why do you double encode the arguments"). So, please ask the HOT website operators/programmers to fix this or at least work together with the JOSM devs (which did not happen in this ticket for ten days from the reporter user pyrog) to point out a problem on JOSM's side (if there is one). Ah, and there is the report on the HOT side ("osm-tasking-manager2") which is still open: <a href="https://github.com/hotosm/osm-tasking-manager2/issues/513">https://github.com/hotosm/osm-tasking-manager2/issues/513</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '15, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '15, 23:01</strong> </span></p>
</div>
</div>
<div id="comments-container-42711" class="comments-container">
&#10;</div>
<div id="comment-tools-42711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42711-form-container" class="comment-form-container">
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


+++
type = "question"
title = "JOSM Validator: Cannot add MapCss rule: Cannot add instruction fixremove"
description = '''I have this JOSM validator mapcss-rule below, which works fine. *[ADDRESS] {  throwerror: tr(&quot;{0} should not be uploaded&quot;, &quot;{0.key}&quot;);  group: tr(&quot;no-import tag&quot;);  /* fixremove: &quot;{0}&quot;; */ }  If I try to uncomment the line with fixremove JOSM gives me this message in the terminal  SEVERE: Cannot add...'''
date = "2019-10-24T20:07:00Z"
lastmod = "2019-10-24T20:07:00Z"
weight = 71322
keywords = [ "josm", "josm-validator", "validator", "mapcss" ]
aliases = [ "/questions/71322" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Validator: Cannot add MapCss rule: Cannot add instruction fixremove](/questions/71322/josm-validator-cannot-add-mapcss-rule-cannot-add-instruction-fixremove)

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
<span id="post-71322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this JOSM validator mapcss-rule below, which works fine.</p>
<pre><code>*[ADDRESS] {
  throwerror: tr(&quot;{0} should not be uploaded&quot;, &quot;{0.key}&quot;);
  group: tr(&quot;no-import tag&quot;);
  /* fixremove: &quot;{0}&quot;; */
}</code></pre>
<p>If I try to uncomment the line with <code>fixremove</code> JOSM gives me this message in the terminal</p>
<pre><code>SEVERE: Cannot add MapCss rule: Cannot add instruction fixremove: {0}!</code></pre>
<p>And this is the same for any value of "fixremove" or "fixadd" I try.</p>
<p>What is the problem here? What do I have to do to get this working?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-josm-validator" rel="tag" title="see questions tagged &#39;josm-validator&#39;">josm-validator</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span> <span class="post-tag tag-link-mapcss" rel="tag" title="see questions tagged &#39;mapcss&#39;">mapcss</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '19, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '19, 20:19</strong> </span></p>
</div>
</div>
<div id="comments-container-71322" class="comments-container">
&#10;</div>
<div id="comment-tools-71322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71322-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


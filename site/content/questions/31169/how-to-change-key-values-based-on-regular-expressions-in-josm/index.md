+++
type = "question"
title = "How to change (key) values based on regular expressions in JOSM"
description = '''Hi I would like to fix simple mistakes in the opening_hours tag based on regular expressions but only if it is clear what they mean … One example (second example on the key page) is opening_hours=0600-1800 → opening_hours=06:00-18:00. An example Python script looks like this: #!/usr/bin/env python #...'''
date = "2014-03-02T15:11:00Z"
lastmod = "2014-03-02T16:48:00Z"
weight = 31169
keywords = [ "python", "josm", "bot", "regex" ]
aliases = [ "/questions/31169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to change (key) values based on regular expressions in JOSM](/questions/31169/how-to-change-key-values-based-on-regular-expressions-in-josm)

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
<span id="post-31169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31169-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I would like to fix simple mistakes in the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours tag</a> based on regular expressions but only if it is clear what they mean … One example (<a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours#Often_made_mistakes">second example on the key page</a>) is opening_hours=0600-1800 → opening_hours=06:00-18:00.</p>
<p>An example Python script looks like this:</p>
<pre><code>#!/usr/bin/env python
# encoding: utf-8
&#10;import re
&#10;wrong = &#39;1200-2300&#39;
&#10;regex = re.compile(r&#39;\A(?P&lt;start_hour&gt;[0-1][0-9]|2[0-4])(?P&lt;start_min&gt;[:1-5][0-9]|0[0-9])\s*(?P&lt;sep&gt;-)\s*(?P&lt;end_hour&gt;[0-1][0-9]|2[0-4])(?P&lt;end_min&gt;[:1-5][0-9]|0[0-9])\Z&#39;)
&#10;re_object = re.search(regex, wrong)
bot_right_val = &#39;%s:%s%s%s:%s&#39; % (
        re_object.group(&#39;start_hour&#39;), re_object.group(&#39;start_min&#39;),
        re_object.group(&#39;sep&#39;),
        re_object.group(&#39;end_hour&#39;), re_object.group(&#39;end_min&#39;)
        )
print &#39;%s -&gt; %s&#39; % (wrong, bot_right_val)</code></pre>
<p>I would like to automate this task a little bit more to avoid chancing this by hand. How can I integrate this script to JOSM? I can already load all wrong values matching this regex with <a href="https://github.com/ypid/opening_hours.js/blob/master/regex_search.py">regex_search.py</a> in JOSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-bot" rel="tag" title="see questions tagged &#39;bot&#39;">bot</span> <span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '14, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b0829ba878989db13885728a5ae8f2bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ypid&#39;s gravatar image" />
<p><span>ypid</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ypid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31169" class="comments-container">
<span id="31170"></span>
<div id="comment-31170" class="comment">
<div id="post-31170-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Just in case you do not know it yet: <span>Automated Edits code of conduct</span>. Your idea sounds like this applies.</p>
</div>
<div id="comment-31170-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 15:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31172"></span>
<div id="comment-31172" class="comment">
<div id="post-31172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> I already read this page. Thanks for the hint. The problem is that I did not really find a description about how to do it. I thought about writing a <a href="https://wiki.openstreetmap.org/w/index.php?title=User:Xybot">Xybot</a> rule file but I wanted to test this first in a simple way.</p>
</div>
<div id="comment-31172-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 15:53)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
<span id="31173"></span>
<div id="comment-31173" class="comment">
<div id="post-31173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The only 'simple' way I came up with is to download all occurrences of a tag in JOSM, save the .osm file, parse and change the file, load the file back to JOSM, upload the file.</p>
</div>
<div id="comment-31173-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 15:55)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
<span id="31174"></span>
<div id="comment-31174" class="comment">
<div id="post-31174-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Okay, fine. So, before you are doing large scale edits, please discuss them (not on this help site).</p>
</div>
<div id="comment-31174-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 15:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31169-form-container" class="comment-form-container">
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

<span id="31176"></span>

<div id="answer-container-31176" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31176-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM has a <span>scripting plugin</span> which supports scripts of various languages. The <span>quality assurance script</span> is a great example for this interface.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '14, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '14, 16:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31176" class="comments-container">
<span id="31177"></span>
<div id="comment-31177" class="comment">
<div id="post-31177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this sounds like the better way. ;-)</p>
</div>
<div id="comment-31177-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 16:40)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31178"></span>
<div id="comment-31178" class="comment">
<div id="post-31178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I might check that out in detail later. For now I will go with the .osm file script variant because I feel more confident in this area.</p>
</div>
<div id="comment-31178-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 16:48)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
</div>
<div id="comment-tools-31176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31171"></span>

<div id="answer-container-31171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31171-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>if you want to use JOSM, my newbie and basic idea (this may be the <em>worst possible way</em>) would be to edit a <span>.osm/JOSM file</span>:</p>
<ol>
<li>Download the data into a .osm file</li>
<li>change the file with your script (just look into a .osm file which contains changes made by JOSM to see how JOSM saves changes - or see the format description, link above)</li>
<li>open and upload with JOSM</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '14, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '14, 16:04</strong> </span></p>
</div>
</div>
<div id="comments-container-31171" class="comments-container">
<span id="31175"></span>
<div id="comment-31175" class="comment">
<div id="post-31175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess this is the way to go.</p>
</div>
<div id="comment-31175-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 15:57)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
<span id="31179"></span>
<div id="comment-31179" class="comment">
<div id="post-31179-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Started to write the script: <a href="https://github.com/ypid/opening_hours_bot">https://github.com/ypid/opening_hours_bot</a></p>
</div>
<div id="comment-31179-info" class="comment-info">
<span class="comment-age">(02 Mar '14, 16:48)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
</div>
<div id="comment-tools-31171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31171-form-container" class="comment-form-container">
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


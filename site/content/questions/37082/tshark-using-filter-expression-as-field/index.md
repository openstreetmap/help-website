+++
type = "question"
title = "tshark: Using filter expression as field ?"
description = '''Hello, I would like to distinguish frames from the tshark output, see this failed attemp : tshark -r mydump-20141015-185000.dump -Y &quot;frame contains a or frame contains b&quot; -T fields -e frame.time -e &quot;frame contains a&quot; -e &quot;frame contains b&quot;  I would like next output: time1 0 1 # not comtains a and con...'''
date = "2014-10-15T11:53:00Z"
lastmod = "2014-10-16T09:20:00Z"
weight = 37082
keywords = [ "fields", "expression", "tshark", "filters" ]
aliases = [ "/questions/37082" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: Using filter expression as field ?](/questions/37082/tshark-using-filter-expression-as-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37082-score" class="post-score" title="current number of votes">0</div><span id="post-37082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to distinguish frames from the tshark output, see this failed attemp :</p><pre><code>tshark -r mydump-20141015-185000.dump  -Y &quot;frame contains a or frame contains b&quot; -T fields -e frame.time -e &quot;frame contains a&quot; -e &quot;frame contains b&quot;</code></pre><p>I would like next output:</p><pre><code>time1 0 1 # not comtains a and contains b
time2 1 1 # contains a and contains b
time3 1 0 # contains a and not contains b</code></pre><p>Thank you very much ! Does tshark have such capabilitie ?</p><p>Un saludo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-expression" rel="tag" title="see questions tagged &#39;expression&#39;">expression</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/ac77c363bbe8e28afbb136d908e9c7f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="i5513&#39;s gravatar image" /><p><span>i5513</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="i5513 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Oct '14, 17:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37082" class="comments-container"></div><div id="comment-tools-37082" class="comment-tools"></div><div class="clear"></div><div id="comment-37082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37086"></span>

<div id="answer-container-37086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37086-score" class="post-score" title="current number of votes">1</div><span id="post-37086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, <code>-e</code> currently supports only fields, not arbitrary filter expressions. File an enhancement request at <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a> if you'd like to see a capability such as this added.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '14, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37086" class="comments-container"><span id="37113"></span><div id="comment-37113" class="comment"><div id="post-37113-score" class="comment-score"></div><div class="comment-text"><p>Forwarded: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10573">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10573</a></p><p>Thank you</p></div><div id="comment-37113-info" class="comment-info"><span class="comment-age">(16 Oct '14, 09:20)</span> <span class="comment-user userinfo">i5513</span></div></div></div><div id="comment-tools-37086" class="comment-tools"></div><div class="clear"></div><div id="comment-37086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


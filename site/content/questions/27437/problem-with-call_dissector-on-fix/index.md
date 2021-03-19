+++
type = "question"
title = "Problem with call_dissector() on fix?"
description = '''Hello, from my protocol I call, depending on the data other protocols ... most of it eth or fix. I made dissector handle static dissector_handle_t data_handle_eth; static dissector_handle_t data_handle_fix;  and used find_dissector on it. data_handle_eth = find_dissector(&quot;eth&quot;); data_handle_fix = fi...'''
date = "2013-11-26T10:00:00Z"
lastmod = "2013-11-26T14:24:00Z"
weight = 27437
keywords = [ "fix", "dissector", "sub-dissector", "error" ]
aliases = [ "/questions/27437" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with call\_dissector() on fix?](/questions/27437/problem-with-call_dissector-on-fix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>from my protocol I call, depending on the data other protocols ... most of it eth or fix.</p><p>I made dissector handle</p><pre><code>static dissector_handle_t data_handle_eth;
static dissector_handle_t data_handle_fix;</code></pre><p>and used find_dissector on it.</p><pre><code>data_handle_eth = find_dissector(&quot;eth&quot;);
data_handle_fix = find_dissector(&quot;fix&quot;);</code></pre><p>when I do</p><pre><code> call_dissector(data_handle_eth, next_tvb, pinfo, tree)</code></pre><p>everything is fine. The data is decoded as eth. But when I do</p><pre><code> call_dissector(data_handle_fix, next_tvb, pinfo, tree)</code></pre><p>wireshark crashes with</p><pre><code> **
 ERROR:packet.c:1988:call_dissector_only: assertion failed: (handle != NULL)
 Aborted</code></pre><p>It can not be a problem with the handler or other code parts from me because when I change</p><pre><code>data_handle_fix = find_dissector(&quot;fix&quot;);</code></pre><p>to tcp or another protocol</p><pre><code>data_handle_fix = find_dissector(&quot;tcp&quot;);</code></pre><p>it works fine with the data.</p><p>Is there a problem with the fix protocol? Any Ideas?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">fix dissector sub-dissector error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/9b1dc01f2575b09d0852f7a4245a0318?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gatherer&#39;s gravatar image" /><p>Gatherer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gatherer has no accepted answers">0%</span></p></div></div><div id="comments-container-27437" class="comments-container"></div><div id="comment-tools-27437" class="comment-tools"></div><div class="clear"></div><div id="comment-27437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27447"></span>

<div id="answer-container-27447" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27447-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably using a version of Wireshark where the fix dissector does not register by name. The fix dissector in trunk has</p><pre><code>fix_handle = new_register_dissector(&quot;fix&quot;, dissect_fix, proto_fix);</code></pre><p>Does that exist in the version you are buildng with?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '13, 14:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-27447" class="comments-container"><span id="27451"></span><div id="comment-27451" class="comment"><div id="post-27451-score" class="comment-score"></div><div class="comment-text"><p>Not unless he's building against the trunk or, possibly, one of the development builds, as per my answer.</p></div><div id="comment-27451-info" class="comment-info"><span class="comment-age">(26 Nov '13, 14:25)</span> Guy Harris ♦♦</div></div><span id="27477"></span><div id="comment-27477" class="comment"><div id="post-27477-score" class="comment-score"></div><div class="comment-text"><p>I will build against different versions ... from 1.2.x to latest stable ... depends on linux version it will run on ...</p><p>So I will try to get fix running by adding the line or some more (now I know the way)</p><p>another small question ... why is it so? Why not register the dissector? Is there a special reason?</p></div><div id="comment-27477-info" class="comment-info"><span class="comment-age">(27 Nov '13, 02:36)</span> Gatherer</div></div><span id="27482"></span><div id="comment-27482" class="comment"><div id="post-27482-score" class="comment-score"></div><div class="comment-text"><p>No other reason than no one needed it before I suspect.</p></div><div id="comment-27482-info" class="comment-info"><span class="comment-age">(27 Nov '13, 04:37)</span> Anders ♦</div></div><span id="27537"></span><div id="comment-27537" class="comment"><div id="post-27537-score" class="comment-score"></div><div class="comment-text"><p>thanks to all ... it is possible to add</p><pre><code> register_dissector(&quot;fix&quot;, dissect_fix, proto_fix);</code></pre><p>in older versions and register fix so it can be found</p></div><div id="comment-27537-info" class="comment-info"><span class="comment-age">(28 Nov '13, 09:08)</span> Gatherer</div></div></div><div id="comment-tools-27447" class="comment-tools"></div><div class="clear"></div><div id="comment-27447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27449"></span>

<div id="answer-container-27449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27449-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a problem with the fix protocol?</p></blockquote><p>No, there's an inadequacy (for your purposes) in the Wireshark dissector for the FIX protocol.</p><p>Unless you're developing the dissector for your protocol to work with the version of Wireshark on the trunk of the SVN repository, or with the current development version of Wireshark, you will <em>NOT</em> be able to call the FIX dissector. Only on the trunk does it register itself by name, in the fashion mentioned by Anders; it does not do so in 1.10.x or in any earlier versions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27449" class="comments-container"></div><div id="comment-tools-27449" class="comment-tools"></div><div class="clear"></div><div id="comment-27449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


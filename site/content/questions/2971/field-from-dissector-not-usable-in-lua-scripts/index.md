+++
type = "question"
title = "field from dissector not usable in lua scripts"
description = '''Here&#x27;s my basic dissector foo_proto = Proto(&quot;foo&quot;,&quot;foo proto&quot;) foo_proto.fields.bar = ProtoField.string(&quot;foo.bar&quot;,&quot;bar field&quot;)  function foo_proto.dissector(buffer,pinfo,tree)  local subtree = tree:add(foo_proto,&quot;Foo Protocol Data&quot;)  subtree:add(foo_proto.fields.bar, pinfo.number) end  register_post...'''
date = "2011-03-21T09:01:00Z"
lastmod = "2011-09-14T05:55:00Z"
weight = 2971
keywords = [ "field", "dissector", "tshark", "lua" ]
aliases = [ "/questions/2971" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [field from dissector not usable in lua scripts](/questions/2971/field-from-dissector-not-usable-in-lua-scripts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2971-score" class="post-score" title="current number of votes">3</div><span id="post-2971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here's my basic dissector</p><pre><code>foo_proto = Proto(&quot;foo&quot;,&quot;foo proto&quot;)
foo_proto.fields.bar = ProtoField.string(&quot;foo.bar&quot;,&quot;bar field&quot;)

function foo_proto.dissector(buffer,pinfo,tree)
   local subtree = tree:add(foo_proto,&quot;Foo Protocol Data&quot;)
   subtree:add(foo_proto.fields.bar, pinfo.number)
end

register_postdissector(foo_proto)</code></pre><p>I use wireshark 1.4.4, I start wireshark and load my dissector in the Lua "Evaluate" window, my packet got dissected correctly and I can see my bar field under the foo proto.</p><p>My problem is that I can't use foo.bar as a filter. When I click on "Expression..." the foo proto appears but it has not fields under. The only filter I can use is: foo</p><p>When try to evaluate:</p><pre><code>  bar_f = Field.new(&quot;foo.bar&quot;)</code></pre><p>I have:</p><pre><code>[string &quot;bar_f = Field.new(&quot;foo.bar&quot;)&quot;]:1: bad argument #1 
 to &#39;new&#39; (Field_new: a field with this name must exist)</code></pre><p>Surprisingly when I use tshark with the option -T fields -e foo.bar and load the lua script, it works, pinfo.number is displayed.</p><p>How can I get my foo.bar field usable in my lua scripts ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/c8966edcf6638b2e16eadbe86a982121?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khshark&#39;s gravatar image" /><p><span>khshark</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '11, 09:03</strong> </span></p></div></div><div id="comments-container-2971" class="comments-container"></div><div id="comment-tools-2971" class="comment-tools"></div><div class="clear"></div><div id="comment-2971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3790"></span>

<div id="answer-container-3790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3790-score" class="post-score" title="current number of votes">1</div><span id="post-3790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I recreated your problem with Wireshark 1.4.6 on Mac OS X 10.6, but it actually works correctly on Windows XP SP3; Windows Wireshark lets me use <code>foo.bar</code> as a filter, and it evaluates <code>Field.new("foo.bar")</code> without error.</p><p>I would <a href="https://bugs.wireshark.org/bugzilla/">submit a bug</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-3790" class="comments-container"></div><div id="comment-tools-3790" class="comment-tools"></div><div class="clear"></div><div id="comment-3790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6358"></span>

<div id="answer-container-6358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6358-score" class="post-score" title="current number of votes">0</div><span id="post-6358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can confirm the original posters problem using Version 1.6.2 (SVN Rev 38931 from /trunk-1.6) x64 under Windows 7 x64 (I used the evaluate function to run both commands)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/56a080ecf59d93993a3cc442743026b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wojtech&#39;s gravatar image" /><p><span>wojtech</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wojtech has no accepted answers">0%</span></p></div></div><div id="comments-container-6358" class="comments-container"></div><div id="comment-tools-6358" class="comment-tools"></div><div class="clear"></div><div id="comment-6358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


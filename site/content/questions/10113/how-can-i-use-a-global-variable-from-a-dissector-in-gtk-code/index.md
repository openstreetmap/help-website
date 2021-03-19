+++
type = "question"
title = "How can I use a global variable from a dissector in gtk code?"
description = '''I have a global variable in a .c file in the dissectors/ folder. How do I use it in another .c file in the gtk/ folder? Every time I try using extern, I get an &quot;undefined reference&quot; error. I am able to use the same variable in another .c file in the epan/ folder. Is there anything I am missing?'''
date = "2012-04-13T01:47:00Z"
lastmod = "2012-04-15T23:37:00Z"
weight = 10113
keywords = [ "development", "gtk", "dissector", "epan" ]
aliases = [ "/questions/10113" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use a global variable from a dissector in gtk code?](/questions/10113/how-can-i-use-a-global-variable-from-a-dissector-in-gtk-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10113-score" class="post-score" title="current number of votes">0</div><span id="post-10113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a global variable in a <code>.c</code> file in the <code>dissectors/</code> folder. How do I use it in another <code>.c</code> file in the <code>gtk/</code> folder? Every time I try using <code>extern</code>, I get an "undefined reference" error. I am able to use the same variable in another <code>.c</code> file in the <code>epan/</code> folder. Is there anything I am missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-epan" rel="tag" title="see questions tagged &#39;epan&#39;">epan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/b7bdcb1b20e2c4bba13948b04439d544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vish&#39;s gravatar image" /><p><span>vish</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '12, 10:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-10113" class="comments-container"></div><div id="comment-tools-10113" class="comment-tools"></div><div class="clear"></div><div id="comment-10113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10137"></span>

<div id="answer-container-10137" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10137-score" class="post-score" title="current number of votes">1</div><span id="post-10137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What is it you're trying to do?</p><p>If the global variable is a parameter setting for your dissector, try just registering it as a preference for the dissector; that way you don't need to write <em>any</em> GUI code for it - the existing Wireshark GUI code will let you set it from the Edit-&gt;Preferences dialog (and you can set it with the <code>-o</code> command-line flag in Wireshark or TShark).</p><p>If you're trying to write a tool to report statistics for your protocol, <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.tapping">the tap mechanism</a> could be used; you wouldn't need a global variable to pass data to a tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10137" class="comments-container"></div><div id="comment-tools-10137" class="comment-tools"></div><div class="clear"></div><div id="comment-10137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10131"></span>

<div id="answer-container-10131" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10131-score" class="post-score" title="current number of votes">0</div><span id="post-10131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what you aim to accomplish sharing something between a dissector and the <code>epan</code> and <code>ui/gtk</code> sections of Wireshark, but if I understand your question correctly, that is not your current problem.</p><p>The <code>extern</code> convention is only really one part of the puzzle you are looking at. At a basic level, the variable needs to both have <em>shared visibility</em> and a <em>single</em> storage area. Before going forward, note that this method will only work if your dissector is built in (which I think it is, since you say it's in <code>epan/dissectors</code> somewhere). Your dissector probably comes in two parts, <code>packet-myproto.c</code> and <code>packet-myproto.h</code>.<br />
To declare the <em>single storage area</em>, you do as you probably already have by declaring <code>int my_global_variable;</code> somewhere in <code>packet-myproto.c</code>. Then, you need to make it accessible to other parts of the application (the <em>shared visibility</em> I mentioned above), and there are two options for doing this:<br />
First, you could simply declare <code>extern int my_global_variable;</code> inside <code>packet-myproto.h</code>, and then <code>#include "packet-myproto.h"</code> in whatever file you need access to the variable, but this poses the issue of also including everything else included by your dissector (almost all of which is probably not needed by your gtk code).<br />
A likely cleaner way of doing this would be to make another file (<code>myproto-globalvariable.h</code> or something) in the same directory with your dissector, then <code>#include</code> that file in <code>packet-myproto.h</code> and in the file for your gtk code. Then, inside the new file simply <code>extern int my_globabl_variable;</code> and you are ready to go. This provides you with the benefit of shared visibility without polluting your global namespace with dissection-related items where they are unneeded.</p><p><strong>In brief</strong>, place the following in each of these files:<br />
<code>epan/dissectors/myproto-helper.h</code>:<br />
</p><blockquote><p><code>extern int my_global_variable;</code></p></blockquote><p><code>epan/dissectors/packet-myproto.h</code>:<br />
</p><blockquote><p><code>#include "myproto-helper.h"</code></p></blockquote><p><code>epan/dissectors/packet-myproto.c</code>:<br />
</p><blockquote><p><code>int my_global_variable;</code></p></blockquote><p><code>path/to/your/gtk/stuff/my_gtk_stuff.c</code>*:</p><blockquote><p><code>#include "../../../../epan/dissectors/myproto-helper.h</code></p></blockquote><p><sub>*It could also be a <code>.h</code> file or what-have-you. Also remember to fix the include path (I'm almost certain <code>../../../../</code> is not correct for your case).</sub></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-10131" class="comments-container"><span id="10168"></span><div id="comment-10168" class="comment"><div id="post-10168-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. But I did as u said but still getting undefined reference to `variable_name' Also its a hash table so I cant add it as a preference. Does it have something related to the Makefile, I mean do I need to give some path so that it looks for it while linking.</p></div><div id="comment-10168-info" class="comment-info"><span class="comment-age">(15 Apr '12, 23:37)</span> <span class="comment-user userinfo">vish</span></div></div></div><div id="comment-tools-10131" class="comment-tools"></div><div class="clear"></div><div id="comment-10131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


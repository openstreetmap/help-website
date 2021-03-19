+++
type = "question"
title = "Wireshark plugin and GPL license"
description = '''Hi,  I&#x27;m expecting to work with Wireshark software in a commercial projet environment.  Wireshark is licensed under the GNU General Public License. But what about the plugin source code I develop for a well-known protocol but specific for our application ?  The source code of Wireshark software is n...'''
date = "2012-07-02T07:16:00Z"
lastmod = "2012-07-03T00:56:00Z"
weight = 12371
keywords = [ "gpl", "license", "plugin" ]
aliases = [ "/questions/12371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark plugin and GPL license](/questions/12371/wireshark-plugin-and-gpl-license)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12371-score" class="post-score" title="current number of votes">0</div><span id="post-12371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm expecting to work with Wireshark software in a commercial projet environment. Wireshark is licensed under the GNU General Public License. But what about the plugin source code I develop for a well-known protocol but specific for our application ? The source code of Wireshark software is not modified and development of the plug-in is not, in my mind, a "derivative work" according to GPL definition. On Lua site, it is written : <a href="http://wiki.wireshark.org/Lua/">http://wiki.wireshark.org/Lua/</a> … Even if the code you write in Lua does not need to be GPL'ed. The code written in Lua that uses bindings to Wireshark must be distributed under the GPL terms... So I don't know ! Any help will be certainly appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gpl" rel="tag" title="see questions tagged &#39;gpl&#39;">gpl</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '12, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/c6601ad12a29acfe5a834160fcc5574f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patcas29&#39;s gravatar image" /><p><span>patcas29</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patcas29 has no accepted answers">0%</span></p></div></div><div id="comments-container-12371" class="comments-container"></div><div id="comment-tools-12371" class="comment-tools"></div><div class="clear"></div><div id="comment-12371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12372"></span>

<div id="answer-container-12372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12372-score" class="post-score" title="current number of votes">1</div><span id="post-12372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would say, you have to apply the GPL to your plugin.</p><p>Reason: <a href="http://www.gnu.org/licenses/gpl-faq.html#GPLPluginsInNF">http://www.gnu.org/licenses/gpl-faq.html#GPLPluginsInNF</a></p><blockquote><p>If the program dynamically links plug-ins, and <strong>they make function calls to each other</strong> and <strong>share data structures</strong>, we believe they form a single program</p></blockquote><p>The marked part is true for a Wireshark plugin.</p><p>Then, you could argue, that the plugin is not really dynamically linked to the main program, as the plugin is loaded at runtime and that's why it is different than in the desription above.</p><p>That might be a valid argument, as also described in that link:</p><blockquote><p>It depends on how the program invokes its plug-ins. If the <strong>program uses fork and exec to invoke plug-ins</strong>, then the plug-ins are separate programs, so the license for the main program makes no requirements for them.</p></blockquote><p>Unfortunately I can't finally answer that one.</p><p>I would tend to say, that your plugin has to be GPLed, as it is using all the internal data structures and the code of Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '12, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '12, 10:03</strong> </span></p></div></div><div id="comments-container-12372" class="comments-container"></div><div id="comment-tools-12372" class="comment-tools"></div><div class="clear"></div><div id="comment-12372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12386"></span>

<div id="answer-container-12386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12386-score" class="post-score" title="current number of votes">1</div><span id="post-12386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Everything using Wireshark's API's, not 'at arms length', is covered by the GPL. That applies to plugins, which are basically an extension of the Ethereal Packet ANalyzer (EPAN) part of *shark. Being 'at arms length' is considered something that interacts through OS means, like a pipe or something.</p><p>Is that a problem? No. Why? Because GPL has to do with <em>distribution</em>. As long as you don't distribute your dissector, you can do what you like. But if you do distribute then your bound by the rule that you have to provide the source code under GPL license.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-12386" class="comments-container"></div><div id="comment-tools-12386" class="comment-tools"></div><div class="clear"></div><div id="comment-12386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


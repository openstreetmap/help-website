+++
type = "question"
title = "Migration of a plugin dissector to 64-bit"
description = '''My task is to create a dissector for my own protocol, implemented as a plugin, compiled to 64-bit architecture. I&#x27;ve been struggling with some errors, and I need some help to complete my work: 1) To successfully build my dissector, do I have to compile the whole Wireshark, or can I just compile my p...'''
date = "2014-07-29T05:23:00Z"
lastmod = "2014-07-29T05:44:00Z"
weight = 34966
keywords = [ "build", "dissector", "visual-studio", "64-bit", "plugin" ]
aliases = [ "/questions/34966" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Migration of a plugin dissector to 64-bit](/questions/34966/migration-of-a-plugin-dissector-to-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34966-score" class="post-score" title="current number of votes">0</div><span id="post-34966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My task is to create a dissector for my own protocol, implemented as a plugin, compiled to 64-bit architecture. I've been struggling with some errors, and I need some help to complete my work:</p><p>1) To successfully build my dissector, do I have to compile the whole Wireshark, or can I just compile my plugin as a dll, and add it to the plugins directory of the downloaded version of WS?</p><p>2)I don't know how makefiles work, and I'm using a Windows7-64bit machine for this project. Can I compile my plugin with Visual Studio, as a standard project, or do I have to deal with these makefiles?</p><p>3)If I can use only Visual Studio, is it possible to use the 2013 vesion, or WS doesn't support it yet, and I have to use a previous version?</p><p>4)once the project is succesfully built to target a 32-bit platform the only thing that I have to do is to change the "Project properties" in order to target a 64-bit platform? Or is there anything else that should be done to produce a 64-bit dissector?</p><p>5)I tried to build my plugin with VS2013, and I have this kind of error: "error LNK2001: unresolved external symbol __ imp _ find _dissector". Is this related to the fact that I am building only the plugin without the whole WS project? Or maybe is that problem about the migration 32-&gt;64? Or maybe something else?</p><p>Thanks a lot in advance for the help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/e1fba327ed394306c1606291dedfd698?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="francesco_bigotto&#39;s gravatar image" /><p><span>francesco_bi...</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="francesco_bigotto has no accepted answers">0%</span></p></div></div><div id="comments-container-34966" class="comments-container"></div><div id="comment-tools-34966" class="comment-tools"></div><div class="clear"></div><div id="comment-34966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34968"></span>

<div id="answer-container-34968" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34968-score" class="post-score" title="current number of votes">1</div><span id="post-34968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="francesco_bigotto has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Arguably none of your questions have much to do with bit width, more to do with building Wireshark. Please read the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/index.html">Developers Guide</a>, read it again, and then follow it exactly.</p><ol><li>Your dissector will need to link with the wireshark library (libwireshark.lib) so you'll have to build all of Wireshark (or at least libwireshark).</li><li>Currently on Windows, Wireshark is built using windows nmake and the makefiles in the sources. The Developers Guide has step-by-step details for building Wireshark.</li><li>The current Wireshark releases use VS2010, but I've been compiling with VS2013 for some time (the makefiles are able to use VS2013) and Wireshark is likely to move to this soon for the next set of releases (post 1.12).</li><li>The platform is set via options provided to the nmake builds. As the builds are "in-tree" changing platform means a "nmake clean" using the old platform settings to remove all the x86 objects, followed by a build with the new platform (or use a separate source tree to have both builds available at the same time).</li><li>See answer #1. Probably. Unlikely. Possibly.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '14, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '14, 06:09</strong> </span></p></div></div><div id="comments-container-34968" class="comments-container"></div><div id="comment-tools-34968" class="comment-tools"></div><div class="clear"></div><div id="comment-34968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


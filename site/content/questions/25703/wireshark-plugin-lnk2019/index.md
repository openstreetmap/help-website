+++
type = "question"
title = "Wireshark plugin LNK2019"
description = '''Dear Wireshark-Community,  I&#x27;ve developed a basic dissector for a protocol. I implemented it as a standard dissector in wireshark. Everything worked pretty well, but now I want to implement this source-code as a plugin. But then I always get this error-message: packet-rasta.obj : error LNK2019: unre...'''
date = "2013-10-07T03:33:00Z"
lastmod = "2013-10-14T09:16:00Z"
weight = 25703
keywords = [ "symbol", "lnk2019", "unresolved", "external", "plugin" ]
aliases = [ "/questions/25703" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark plugin LNK2019](/questions/25703/wireshark-plugin-lnk2019)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25703-score" class="post-score" title="current number of votes">0</div><span id="post-25703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark-Community,</p><p>I've developed a basic dissector for a protocol. I implemented it as a standard dissector in wireshark. Everything worked pretty well, but now I want to implement this source-code as a plugin. But then I always get this error-message:</p><p><em>packet-rasta.obj : error LNK2019: unresolved external symbol _imp_register_dissector referenced in funktion _proto_register_rasta</em></p><p><em>packet-rasta.obj : error LNK2019: unresolved external symbol _imp_proto_register_subtree_array referenced in funktion _proto_register_rasta</em></p><p><em>...</em></p><p>This message appears almost at every funktion, overall 14 unresolved external symbols. I use Win7 and MSVS2010, all changes in Makefiel.am, Makefile.nmake and so on have been made and are correct. Can somebody healp me...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-symbol" rel="tag" title="see questions tagged &#39;symbol&#39;">symbol</span> <span class="post-tag tag-link-lnk2019" rel="tag" title="see questions tagged &#39;lnk2019&#39;">lnk2019</span> <span class="post-tag tag-link-unresolved" rel="tag" title="see questions tagged &#39;unresolved&#39;">unresolved</span> <span class="post-tag tag-link-external" rel="tag" title="see questions tagged &#39;external&#39;">external</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '13, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/29dda1a3f1a92e1755318de9e31696c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko1988&#39;s gravatar image" /><p><span>Marko1988</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko1988 has no accepted answers">0%</span></p></div></div><div id="comments-container-25703" class="comments-container"><span id="25970"></span><div id="comment-25970" class="comment"><div id="post-25970-score" class="comment-score"></div><div class="comment-text"><p>You may want to pattern your Makefile.nmake after the one in the plugins/gryphon directory. Copy those Makefiles (including Makefile.common, etc.) to your own dissector and then make only the changes needed to refer to your protocol. That's usually the cleanest way to resolve linking issues.</p></div><div id="comment-25970-info" class="comment-info"><span class="comment-age">(14 Oct '13, 09:16)</span> <span class="comment-user userinfo">beroset</span></div></div></div><div id="comment-tools-25703" class="comment-tools"></div><div class="clear"></div><div id="comment-25703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


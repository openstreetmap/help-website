+++
type = "question"
title = "Couldnt load module:  undefinded symbol: dissector_add"
description = '''Hi, i try to make a plugin based ASN1 dissector. I used the toyasn1 sample and only added my .asn files to the makefile of the Plugin. Now if i start wireshark i always get the error: Couldn&#x27;t load module /wireshark-1.10-9/plugins/toyasn1/.libs/toyasn1.so: /wireshark-1.10.9/plugins/toyasn1/.libs/toy...'''
date = "2014-09-11T01:54:00Z"
lastmod = "2014-09-11T09:14:00Z"
weight = 36193
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/36193" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Couldnt load module: undefinded symbol: dissector\_add](/questions/36193/couldnt-load-module-undefinded-symbol-dissector_add)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36193-score" class="post-score" title="current number of votes">0</div><span id="post-36193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i try to make a plugin based ASN1 dissector. I used the toyasn1 sample and only added my .asn files to the makefile of the Plugin. Now if i start wireshark i always get the error: <code>Couldn't load module /wireshark-1.10-9/plugins/toyasn1/.libs/toyasn1.so: /wireshark-1.10.9/plugins/toyasn1/.libs/toysn1.so: undefined symbol: dissector_add</code></p><p>The same error occours with dissector_delete.</p><p>Does someone know how to solve it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '14, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/f65ac046295141d9f33ce4ac1770b5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venturina&#39;s gravatar image" /><p><span>Venturina</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venturina has no accepted answers">0%</span></p></div></div><div id="comments-container-36193" class="comments-container"></div><div id="comment-tools-36193" class="comment-tools"></div><div class="clear"></div><div id="comment-36193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36196"></span>

<div id="answer-container-36196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36196-score" class="post-score" title="current number of votes">2</div><span id="post-36196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The api changed to <code>dissector_add_uint()</code> I believe.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '14, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Sep '14, 04:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36196" class="comments-container"><span id="36197"></span><div id="comment-36197" class="comment"><div id="post-36197-score" class="comment-score"></div><div class="comment-text"><p>Ah ok, thanks, i think you are right. But now, i get the same Error with <code>undefined Symbol: dissector_add_unit</code></p><p>I don't know what that error means.</p></div><div id="comment-36197-info" class="comment-info"><span class="comment-age">(11 Sep '14, 04:04)</span> <span class="comment-user userinfo">Venturina</span></div></div><span id="36199"></span><div id="comment-36199" class="comment"><div id="post-36199-score" class="comment-score"></div><div class="comment-text"><p>_uint, not _unit</p></div><div id="comment-36199-info" class="comment-info"><span class="comment-age">(11 Sep '14, 04:20)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="36201"></span><div id="comment-36201" class="comment"><div id="post-36201-score" class="comment-score"></div><div class="comment-text"><p>Aww.. thats right. Sometimes reading is difficult.</p><p>Now i geht the Error <code>undefined symbol: dissect_TOYASN1_MESSAGE_PDU</code></p><p>I think this problem lies in my toyasn1.cnf right?</p><p>Because i changed the .asn input files, the <code>dissect_TOYASN1_MESSAGE_PDU</code> function ist not created. My .asn files are <code>CAM.asn</code> and <code>ITS-Containor.asn</code>. In an other dissector, the <code>dissect_name_PDU</code> is created in the <code>packet-name-fn.c</code> file, but in my file is no such function</p><p>thank you very much for your help!</p></div><div id="comment-36201-info" class="comment-info"><span class="comment-age">(11 Sep '14, 05:00)</span> <span class="comment-user userinfo">Venturina</span></div></div><span id="36205"></span><div id="comment-36205" class="comment"><div id="post-36205-score" class="comment-score"></div><div class="comment-text"><p>See the answers in this thread: <a href="https://ask.wireshark.org/questions/36092/asn1-plugin-dissector">https://ask.wireshark.org/questions/36092/asn1-plugin-dissector</a></p></div><div id="comment-36205-info" class="comment-info"><span class="comment-age">(11 Sep '14, 09:14)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-36196" class="comment-tools"></div><div class="clear"></div><div id="comment-36196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


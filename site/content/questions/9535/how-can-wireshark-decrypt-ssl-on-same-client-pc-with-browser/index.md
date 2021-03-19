+++
type = "question"
title = "How can Wireshark decrypt SSL on same client PC with browser?"
description = '''Is there a way to pair up my instance of Wireshark with the Browser running on my PC so that I can decrypt my own SSL sessions? I&#x27;m not trying to feed other captures to my instance of Wireshark. It just seems that on the same PC that is able to conduct the SSL session there should be a way for Wires...'''
date = "2012-03-14T07:11:00Z"
lastmod = "2012-03-15T05:42:00Z"
weight = 9535
keywords = [ "ssl", "decrypt" ]
aliases = [ "/questions/9535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can Wireshark decrypt SSL on same client PC with browser?](/questions/9535/how-can-wireshark-decrypt-ssl-on-same-client-pc-with-browser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9535-score" class="post-score" title="current number of votes">0</div><span id="post-9535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to pair up my instance of Wireshark with the Browser running on my PC so that I can decrypt my own SSL sessions? I'm not trying to feed other captures to my instance of Wireshark. It just seems that on the same PC that is able to conduct the SSL session there should be a way for Wireshark to be able to have access to the decrypted payloads. I'd really like to pair this up with Firebug/Firefox so that I can make sense of SSL/HTTPS packet flows for multi-object web page performance analysis. Today I'm unable to precisely analyze the packets for the elements conducted within such a TCP session.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '12, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/7bb2a6bc57e437eb644353a639170430?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichardBerke&#39;s gravatar image" /><p><span>RichardBerke</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichardBerke has no accepted answers">0%</span></p></div></div><div id="comments-container-9535" class="comments-container"><span id="9543"></span><div id="comment-9543" class="comment"><div id="post-9543-score" class="comment-score"></div><div class="comment-text"><p>I saw the posts about SSL decryption when you have the private keys manually. I don't have and can't get them. The servers are Production, and sometimes (often) not in my company. Somehow my Browser is able to conduct sessions okay with the servers I aim to. I want somehow to have Wireshark's rich TCP related troubleshooting of the packets of my own system, that my own system already knows how to interpret up at the Browser. I don't see how to do that. Maybe there isn't a way today (Wireshark 1.7).</p></div><div id="comment-9543-info" class="comment-info"><span class="comment-age">(14 Mar '12, 12:21)</span> <span class="comment-user userinfo">RichardBerke</span></div></div></div><div id="comment-tools-9535" class="comment-tools"></div><div class="clear"></div><div id="comment-9535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9536"></span>

<div id="answer-container-9536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9536-score" class="post-score" title="current number of votes">2</div><span id="post-9536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As long as you have the private key of the server, you can decrypt the session. See the wiki page <a href="http://wiki.wireshark.org/SSL">SSL</a> for more info, or see the answers to <a href="http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">this</a> question which apparently allow you to do this with the "openssl s_client" output.</p><p>Edit. Presuming your comment was in response to this answer, I've found some more info:</p><p>There is a reason that it's difficult to get access to the contents of a protected SSL/TLS conversation and it's called security :-)</p><p>The question I linked to shows that using the open ssl client utility instead of a browser allows the export of key info that can be used to decrypt the conversation.</p><p>The info in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4349">bug 4349</a> also indicates that a specially built debug version of Firefox (or more specifically the NSS library used by FF) can output key info allowing Wireshark to decrypt the conversation.</p><p>Another option might be to install <a href="http://www.fiddler2.com/fiddler2/">Fiddler</a>, a web debugging proxy, but I don't think this will allow Wireshark captures of the decrypted conversation on Windows, but might on other OS's that can capture on 'loopback' connections.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '12, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '12, 14:17</strong> </span></p></div></div><div id="comments-container-9536" class="comments-container"><span id="9553"></span><div id="comment-9553" class="comment"><div id="post-9553-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. I'll read up some more about OpenSSL and getting the key so Wireshark can use it. That thread about bug 4349 sounds interesting, too.</p><p>I understand Fiddler is/provides a proxy, but I'd expect Wireshark to only see packets right before the network card, where they'd still be encrypted.</p><p>Richard</p></div><div id="comment-9553-info" class="comment-info"><span class="comment-age">(15 Mar '12, 04:55)</span> <span class="comment-user userinfo">RichardBerke</span></div></div><span id="9554"></span><div id="comment-9554" class="comment"><div id="post-9554-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment as that's how this site works, see the <a href="http://ask.wireshark.org/faq/">FAQ</a>.</p><p>The way a proxy works it will create a socket on the local machine (127.0.0.1) that the browser connects to. On Windows this traffic is nigh on impossible to capture, but I think can be done on other OS's.</p></div><div id="comment-9554-info" class="comment-info"><span class="comment-age">(15 Mar '12, 05:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9536" class="comment-tools"></div><div class="clear"></div><div id="comment-9536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


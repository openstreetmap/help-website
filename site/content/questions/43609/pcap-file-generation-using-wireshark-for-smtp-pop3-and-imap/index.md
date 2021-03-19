+++
type = "question"
title = "PCAP file generation using wireshark for SMTP, POP3 and IMAP"
description = '''How do i generate pcap files for protocols such as SMTP, POP3 and IMAP. I need to send a email with attachments and capture the same as pcap file. I dont know how to generate pcap file for above mentioned protocols. Please help me out.'''
date = "2015-06-27T15:56:00Z"
lastmod = "2015-07-08T12:21:00Z"
weight = 43609
keywords = [ "pop3", "pcap", "smtp", "imap", "wireshark" ]
aliases = [ "/questions/43609" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP file generation using wireshark for SMTP, POP3 and IMAP](/questions/43609/pcap-file-generation-using-wireshark-for-smtp-pop3-and-imap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43609-score" class="post-score" title="current number of votes">0</div><span id="post-43609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do i generate pcap files for protocols such as SMTP, POP3 and IMAP. I need to send a email with attachments and capture the same as pcap file. I dont know how to generate pcap file for above mentioned protocols. Please help me out.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pop3" rel="tag" title="see questions tagged &#39;pop3&#39;">pop3</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-imap" rel="tag" title="see questions tagged &#39;imap&#39;">imap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '15, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/01dc4abf2dc404ecc82284d9a3879637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kruthi&#39;s gravatar image" /><p><span>kruthi</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kruthi has no accepted answers">0%</span></p></div></div><div id="comments-container-43609" class="comments-container"><span id="43643"></span><div id="comment-43643" class="comment"><div id="post-43643-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I need to send a email with attachments and capture the same as pcap file. <strong>I dont know how to generate pcap file for above mentioned protocols.</strong></p></blockquote><p>How do you do that? Well, by sending an e-mail from A to B via SMTP and by capturing that traffic between A and B. Same for POP3, IMAP for the e-mail download.</p><p>This sounds a bit like a homework assignment, and you are trying to take the easy route by crafting a pcap file instead of doing the whole E-Mail part ;-)) Am I right with my assumption?</p></div><div id="comment-43643-info" class="comment-info"><span class="comment-age">(28 Jun '15, 17:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43979"></span><div id="comment-43979" class="comment"><div id="post-43979-score" class="comment-score"></div><div class="comment-text"><p>I am not woking on any assignment, actually i am working on xplico and different protocols it can support so in order to check what all protocols it supports i need pcap files to run against xplico with different scenarios. I found some pcap files but without file attachments so wanted to know how to generate pcap file with file attachments.</p></div><div id="comment-43979-info" class="comment-info"><span class="comment-age">(08 Jul '15, 12:21)</span> <span class="comment-user userinfo">kruthi</span></div></div></div><div id="comment-tools-43609" class="comment-tools"></div><div class="clear"></div><div id="comment-43609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43622"></span>

<div id="answer-container-43622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43622-score" class="post-score" title="current number of votes">1</div><span id="post-43622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure whether I understand the question correctly. With "generate pcap files" you mean capturing traffic?<br />
And your question is more like<br />
"I want to filter my capture to only contain traffic that contains SMTP,POP3 and IMAP protocol"<br />
The filter on those packets would be: tcp.port==25 or tcp.port==109 or tcp.port==1010<br />
Or is your problem:<br />
"I already captured traffic but I can't find SMTP,POP3 and IMAP protocol in the trace file even though I was sending an e-mail with attachment while the trace was running"<br />
The reason might be that email traffic today is encrypted using TLS so you won't be able to identify the TLS secured e-mail protocols.<br />
Can you please clarify your question, regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-43622" class="comments-container"><span id="43677"></span><div id="comment-43677" class="comment"><div id="post-43677-score" class="comment-score"></div><div class="comment-text"><p>Actually, if you can obtain the SSL secrets, Wireshark is able to decrypt those captures. See <a href="https://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">https://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys</a> for some examples.</p></div><div id="comment-43677-info" class="comment-info"><span class="comment-age">(29 Jun '15, 10:03)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-43622" class="comment-tools"></div><div class="clear"></div><div id="comment-43622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


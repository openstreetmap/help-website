+++
type = "question"
title = "Where to find documentation of writing an encapsulated file reader"
description = '''Hi I am working on a file reader that can read dump files containing ETSI (Ber encoded) data and .... struggling. Especially when trying to dissect the data. I already implemented a dissector, a simple ber-based reader and a packet-encap file, but the dissection mechanism, and how to call the dissec...'''
date = "2012-07-12T07:50:00Z"
lastmod = "2012-07-13T18:07:00Z"
weight = 12660
keywords = [ "encapsulation", "dissector", "documentation" ]
aliases = [ "/questions/12660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where to find documentation of writing an encapsulated file reader](/questions/12660/where-to-find-documentation-of-writing-an-encapsulated-file-reader)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12660-score" class="post-score" title="current number of votes">0</div><span id="post-12660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am working on a file reader that can read dump files containing ETSI (Ber encoded) data and .... struggling. Especially when trying to dissect the data. I already implemented a dissector, a simple ber-based reader and a packet-encap file, but the dissection mechanism, and how to call the dissector is still a bit of a mystery to me. Any documentation / examples / tips are welcome.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-documentation" rel="tag" title="see questions tagged &#39;documentation&#39;">documentation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '12, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/f7b86af5c2a0a5df465eb1203761ce1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michel&#39;s gravatar image" /><p><span>Michel</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michel has no accepted answers">0%</span></p></div></div><div id="comments-container-12660" class="comments-container"><span id="12679"></span><div id="comment-12679" class="comment"><div id="post-12679-score" class="comment-score"></div><div class="comment-text"><p>So what do you mean by "a simple BER-based reader" and "a packet-encap file"? Presumably you have a file that plugs into the Wiretap library to read the file (although if it's just BER-encoded data and the top-level encoding is a SET or a SEQUENCE or a CONTEXT less than 32, there's already code in Wireshark to read it - <code>wiretap/ber.c</code>), and a dissector for the BER-encoded data; is the issue one of connecting the two, so that the contents of the file are dissected by your dissector?)</p></div><div id="comment-12679-info" class="comment-info"><span class="comment-age">(12 Jul '12, 19:54)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="12697"></span><div id="comment-12697" class="comment"><div id="post-12697-score" class="comment-score"></div><div class="comment-text"><p>I am trying to create a reader to read a dump file containing ber encoded tlv packets (etsi protocol). The ber.c reader can read some packets from my dump file, but is not capable of reading the entire dump itself, and has some packet size restrictions. So, I have to create a reader of my own.</p><p>Furthermore I use the mime_file, packet-mime-encap.c and packet-image-jfif.c as an example to find out how the dissector call mechanism works.</p><p>Thus I am in the assumption that I need a packet-etsi-encap.c file to do the trick, but I am not sure if I am on the right track.</p></div><div id="comment-12697-info" class="comment-info"><span class="comment-age">(13 Jul '12, 01:35)</span> <span class="comment-user userinfo">Michel</span></div></div></div><div id="comment-tools-12660" class="comment-tools"></div><div class="clear"></div><div id="comment-12660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12714"></span>

<div id="answer-container-12714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12714-score" class="post-score" title="current number of votes">0</div><span id="post-12714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So what you'd probably need to do here is:</p><ol><li>add a new <code>WTAP_ENCAP_</code> value in <code>wiretap/wtap.h</code> for the packet format your reader provides, and have the reader supply that as the packet encapsulation value;</li><li>add a new dissector that recognizes that packet format;</li><li>have the dissector register in the <code>"wtap_encap"</code> dissector table with the new <code>WTAP_ENCAP_</code> value.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '12, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12714" class="comments-container"></div><div id="comment-tools-12714" class="comment-tools"></div><div class="clear"></div><div id="comment-12714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


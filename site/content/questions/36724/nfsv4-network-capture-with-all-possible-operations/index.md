+++
type = "question"
title = "NFSv4 network capture with all possible operations"
description = '''I&#x27;m working on NFSv3/4 network utility and for testing purposes I am looking for NFSv4 captures containing all possible NFSv4 operations. I found a &quot;Fairly complete trace of all NFS v3 packet types&quot; here http://wiki.wireshark.org/SampleCaptures#NFS_Protocol_Family I googled a lot but I can not find ...'''
date = "2014-09-30T08:02:00Z"
lastmod = "2014-10-02T00:03:00Z"
weight = 36724
keywords = [ "nfs" ]
aliases = [ "/questions/36724" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [NFSv4 network capture with all possible operations](/questions/36724/nfsv4-network-capture-with-all-possible-operations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36724-score" class="post-score" title="current number of votes">0</div><span id="post-36724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on NFSv3/4 network utility and for testing purposes I am looking for NFSv4 captures containing all possible NFSv4 operations.</p><p>I found a "Fairly complete trace of all NFS v3 packet types" here <a href="http://wiki.wireshark.org/SampleCaptures#NFS_Protocol_Family">http://wiki.wireshark.org/SampleCaptures#NFS_Protocol_Family</a></p><p>I googled a lot but I can not find something similar for NFSv4.</p><p>Yes, off course most of NFSv4 operations I was able to easily reproduce by myself.</p><p>But I don't know how too make these: CREATE, LINK, LOCK, LOCKT, LOCKU, NVERIFY, OPENATTR, OPEN_DOWNGRADE, READ, READLINK, SECINFO, VERIFY, RELEASE_LOCKOWNER, GET_DIR_DELEGATION.</p><p>Maybe someone can share with me some kind of "NFSv4_all_operations_capture.pcap" or tell me the way to reproduce them?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfs" rel="tag" title="see questions tagged &#39;nfs&#39;">nfs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/f80e08d89f48446d813e06745c941669?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexey%20Costroma&#39;s gravatar image" /><p><span>Alexey Costroma</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexey Costroma has no accepted answers">0%</span></p></div></div><div id="comments-container-36724" class="comments-container"></div><div id="comment-tools-36724" class="comment-tools"></div><div class="clear"></div><div id="comment-36724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36760"></span>

<div id="answer-container-36760" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36760-score" class="post-score" title="current number of votes">1</div><span id="post-36760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alexey Costroma has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The following is a list of nfsv4 opcodes found in nfs captures posted to Wireshark bugzilla.</p><p>You can use the "Custom Search" function under the "Not so simple search" tab of the bugzilla search screen to find the bug to which the file is attached. (Don't include the initial leading "digits-" in the filename being searched for".</p><p>Note that you must select all the fields under resolution for the search to succeed.</p><pre><code>392-nfs4.pcap.gz:
   ACCESS
   CLOSE
   COMMIT
   CREATE
   DELEGRETURN
   GETATTR
   GETFH
   LINK
   LOOKUP
   OPEN
   OPEN_CONFIRM
   PUTFH
   READ
   READDIR
   READLINK
   REMOVE
   RENAME
   SAVEFH
   SETATTR
   WRITE

716-NFSv4_SETATTR.cap:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   NVERIFY
   PUTFH
   SETATTR

740-v4.snoop:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   NVERIFY
   PUTFH
   SETATTR

743-NFSv4.cap:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   NVERIFY
   PUTFH
   SETATTR

1173-nfsv4_getattr_fslocations.trc:
   GETATTR
   LOOKUP
   PUTFH

1438-nfs4.1sample.pcap:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   PUTFH
   PUTROOTFH
   READDIR
   REMOVE
   EXCHANGE_ID
   CREATE_SESSION
   SEQUENCE

2269-nfsv4_getattr_req_response.trc:
   GETATTR
   PUTROOTFH

4289-reclaim_complete.cap:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   OPEN
   PUTFH
   PUTROOTFH
   RESTOREFH
   SAVEFH
   SETATTR
   EXCHANGE_ID
   CREATE_SESSION
   DESTROY_SESSION
   SEQUENCE
   RECLAIM_COMPLETE

4713-CelerraNFSv4FH.pcap:
   ACCESS
   CLOSE
   GETATTR
   GETFH
   LOCK
   LOCKU
   LOOKUP
   OPEN
   OPEN_CONFIRM
   PUTFH
   PUTROOTFH
   READ
   RESTOREFH
   SAVEFH
   SETCLIENTID
   SETCLIENTID_CONFIRM

4743-NFSv4--Reads-and-Writes.cap.gz:
   CLOSE
   COMMIT
   GETATTR
   GETFH
   LOOKUP
   OPEN
   PUTFH
   READ
   RESTOREFH
   SAVEFH
   SETATTR
   WRITE

5153-setclientid-bug-in-3079.cap.gz:
   ACCESS
   GETATTR
   GETFH
   LOOKUP
   LOOKUPP
   NVERIFY
   PUTFH
   PUTROOTFH
   READDIR
   RESTOREFH
   SAVEFH
   SECINFO
   SETCLIENTID
   SETCLIENTID_CONFIRM

5741-test_find4.cap:
   ACCESS
   CLOSE
   COMMIT
   GETATTR
   GETFH
   LOOKUP
   OPEN
   OPEN_CONFIRM
   PUTFH
   READ
   READDIR
   RESTOREFH
   SAVEFH
   SETATTR
   WRITE

8245-pnfs.pcap:
   GETATTR
   PUTFH
   LAYOUTCOMMIT
   LAYOUTGET
   SEQUENCE

8717-trim-lone-packet-obfuscated:
   GETATTR
   GETFH
   OPEN
   PUTFH

8720-trim-lone-packet-obfuscated-v2.pcap:
   GETATTR
   GETFH
   OPEN
   PUTFH

9711-free-stateid-and-open-why-no-deleg-example.pcap:
   CLOSE
   GETFH
   LOOKUP
   OPEN
   PUTROOTFH
   FREE_STATEID
   SEQUENCE

10451-fslocation.pcap:
   ACCESS
   CLOSE
   COMMIT
   CREATE
   GETATTR
   GETFH
   LINK
   LOCK
   LOCKT
   LOCKU
   LOOKUP
   LOOKUPP
   NVERIFY
   OPEN
   OPEN_CONFIRM
   OPEN_DOWNGRADE
   PUTFH
   PUTPUBFH
   PUTROOTFH
   READ
   READDIR
   READLINK
   REMOVE
   RENAME
   RENEW
   RESTOREFH
   SAVEFH
   SECINFO
   SETATTR
   SETCLIENTID
   SETCLIENTID_CONFIRM
   VERIFY
   WRITE
   RELEASE_LOCKOWNER

10578-acls.cap:
   GETATTR
   PUTFH

10591-cb_sequence.pcap:
   EXCHANGE_ID
   CREATE_SESSION

10595-open-wants.pcap:
   GETFH
   LOOKUP
   OPEN
   PUTROOTFH
   SEQUENCE

11068-wireshark_nfs4bug_example.trc:
   ACCESS
   CLOSE
   GETATTR
   GETFH
   LOOKUP
   OPEN
   PUTFH
   PUTROOTFH
   READDIR
   REMOVE
   RENAME
   RENEW
   RESTOREFH
   SAVEFH
   SETATTR
   SETCLIENTID
   SETCLIENTID_CONFIRM
   WRITE</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-36760" class="comments-container"><span id="36775"></span><div id="comment-36775" class="comment"><div id="post-36775-score" class="comment-score"></div><div class="comment-text"><p>That's great! Thank you!</p></div><div id="comment-36775-info" class="comment-info"><span class="comment-age">(02 Oct '14, 00:03)</span> <span class="comment-user userinfo">Alexey Costroma</span></div></div></div><div id="comment-tools-36760" class="comment-tools"></div><div class="clear"></div><div id="comment-36760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36732"></span>

<div id="answer-container-36732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36732-score" class="post-score" title="current number of votes">0</div><span id="post-36732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try <a href="http://pcapr.net/home">pcapr.net</a>. There are a number of NFS capture files there. Most of them are v2 or v3, but one of them is specifically listed as being v4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '14, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-36732" class="comments-container"><span id="36744"></span><div id="comment-36744" class="comment"><div id="post-36744-score" class="comment-score"></div><div class="comment-text"><p>I've already tried (( Well I've found several small NFSv4 traces, but there was only NVERIFY and some other operations that I already have.</p><p>Unfortunatelly they don't contain CREATE, LINK, LOCK, LOCKT, LOCKU, OPENATTR, OPEN_DOWNGRADE, READ, READLINK, SECINFO, VERIFY, RELEASE_LOCKOWNER, GET_DIR_DELEGATION</p></div><div id="comment-36744-info" class="comment-info"><span class="comment-age">(30 Sep '14, 23:30)</span> <span class="comment-user userinfo">Alexey Costroma</span></div></div></div><div id="comment-tools-36732" class="comment-tools"></div><div class="clear"></div><div id="comment-36732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


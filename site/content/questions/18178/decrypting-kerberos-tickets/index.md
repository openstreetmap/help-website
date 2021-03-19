+++
type = "question"
title = "Decrypting Kerberos tickets"
description = '''I&#x27;m doing a network capture using wireshark targeting some Kerberos traffic (ticket cache is flushed, then a request is made to a file server - thus generating the AS-REQ/AS-REP/TGS-REQ/TGS-REP sequences) and I&#x27;d like to see the encrypted parts of the tickets (eg timestamps used as authenticators). ...'''
date = "2013-01-31T04:28:00Z"
lastmod = "2013-01-31T04:28:00Z"
weight = 18178
keywords = [ "decryption", "kerberos", "keytab" ]
aliases = [ "/questions/18178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting Kerberos tickets](/questions/18178/decrypting-kerberos-tickets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18178-score" class="post-score" title="current number of votes">0</div><span id="post-18178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm doing a network capture using wireshark targeting some Kerberos traffic (ticket cache is flushed, then a request is made to a file server - thus generating the AS-REQ/AS-REP/TGS-REQ/TGS-REP sequences) and I'd like to see the encrypted parts of the tickets (eg timestamps used as authenticators). I've found <a href="http://i1.blogs.msdn.com/b/spatdsg/archive/2009/03/26/more-kerberos-fun-with-pac-s.aspx">http://i1.blogs.msdn.com/b/spatdsg/archive/2009/03/26/more-kerberos-fun-with-pac-s.aspx</a> which is pretty straightforward. However, by doing the steps presented there, the encrypted part is never decrypted. Wireshark works just fine, because with its own samples, decoding works great (<a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=krb-816.zip).">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=krb-816.zip).</a> So obviously there must be something wrong in the process. The client I'm using is a Windows 7, against a 2008 R2 DC. I tried exporting the keytab under different encryption formats (both RC4-HMAC-NT and AES256-SHA1) using my own principal name using ktpass, but neither worked. Could you help me figure out what's wrong ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-kerberos" rel="tag" title="see questions tagged &#39;kerberos&#39;">kerberos</span> <span class="post-tag tag-link-keytab" rel="tag" title="see questions tagged &#39;keytab&#39;">keytab</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/3bd14a3e7ad36f6938d557b00b525634?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mihai%20Albert&#39;s gravatar image" /><p><span>Mihai Albert</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mihai Albert has no accepted answers">0%</span></p></div></div><div id="comments-container-18178" class="comments-container"></div><div id="comment-tools-18178" class="comment-tools"></div><div class="clear"></div><div id="comment-18178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


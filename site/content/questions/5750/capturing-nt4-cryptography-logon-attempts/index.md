+++
type = "question"
title = "capturing nt4 cryptography logon attempts?"
description = '''Is there a way to configure wireshark to capture NT4 cryptography logon attempts? We are in the final steps before upgrading our Active Directory environment and we want to identify and decommision any outdated boxes without reducing the security level of our environment. Any help would be appreciat...'''
date = "2011-08-18T16:30:00Z"
lastmod = "2011-08-20T03:22:00Z"
weight = 5750
keywords = [ "capture", "logon", "nt4", "cryptography" ]
aliases = [ "/questions/5750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capturing nt4 cryptography logon attempts?](/questions/5750/capturing-nt4-cryptography-logon-attempts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5750-score" class="post-score" title="current number of votes">0</div><span id="post-5750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to configure wireshark to capture NT4 cryptography logon attempts? We are in the final steps before upgrading our Active Directory environment and we want to identify and decommision any outdated boxes without reducing the security level of our environment. Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-logon" rel="tag" title="see questions tagged &#39;logon&#39;">logon</span> <span class="post-tag tag-link-nt4" rel="tag" title="see questions tagged &#39;nt4&#39;">nt4</span> <span class="post-tag tag-link-cryptography" rel="tag" title="see questions tagged &#39;cryptography&#39;">cryptography</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '11, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/2039332d1cc2f5c324f234a92955b5ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="worldzfree&#39;s gravatar image" /><p><span>worldzfree</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="worldzfree has no accepted answers">0%</span></p></div></div><div id="comments-container-5750" class="comments-container"></div><div id="comment-tools-5750" class="comment-tools"></div><div class="clear"></div><div id="comment-5750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5777"></span>

<div id="answer-container-5777" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5777-score" class="post-score" title="current number of votes">0</div><span id="post-5777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What exactly do you mean with "NT4 cyrptography logon attempt"?</p><p>SMB sessions are established in multiple phases. The general workflow is this:</p><p>Establish TCP session -&gt; Establish NetBIOS session -&gt; Negotiate Protocol -&gt; Session setup</p><p>Note that NT4 and older systems will only use TCP port 139 while newer systems also use TCP port 445. When using TCP port 445 no extra packets are exchanged to establish a NetBIOS session.</p><p>The multitude of authentication methods is negotiated during the session setup, which is found with the Wireshark filter <strong>smb.cmd == 0x73</strong></p><p>Lucky for you, operating systems can be identified in the early phases of session setup. Wireshark displays the operating system in the field <strong>smb.native_lanman</strong></p><p>One easy way to identify all the operating systems observed at your capture point is this handy spell:</p><p><strong><code>tshark -r myfile.pcap -R  "smb.cmd==0x73 and smb.native_lanman" -Tfields -e ip.src -e smb.native_lanman</code></strong></p><p>If you are running under Linux/Unix you can pipe the output to a sort command:</p><p><strong><code>tshark -r myfile.pcap -R  "smb.cmd==0x73 and smb.native_lanman" -Tfields -e ip.src -e smb.native_lanman | sort | uniq -c</code></strong></p><p>voila.</p><p>Hth, Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '11, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-5777" class="comments-container"></div><div id="comment-tools-5777" class="comment-tools"></div><div class="clear"></div><div id="comment-5777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


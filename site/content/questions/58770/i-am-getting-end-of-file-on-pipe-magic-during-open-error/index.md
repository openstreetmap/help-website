+++
type = "question"
title = "I am getting &quot;End of file on pipe magic during open.&quot; error."
description = '''So i have proxy in the cloud and im accessing it with ssh and now when i want to use wireshark to start capturing traffic on that proxy i must start tshark in that server. Code : wireshark -k -i &amp;lt;(ssh ServerUserName@proxyip &quot;tshark -F pcap -w - -f &#x27;not tcp port x&#x27;&quot;) This is what i get in terminal...'''
date = "2017-01-15T07:05:00Z"
lastmod = "2017-01-15T07:05:00Z"
weight = 58770
keywords = [ "tshark", "ssh", "wireshark" ]
aliases = [ "/questions/58770" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I am getting "End of file on pipe magic during open." error.](/questions/58770/i-am-getting-end-of-file-on-pipe-magic-during-open-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58770-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So i have proxy in the cloud and im accessing it with ssh and now when i want to use wireshark to start capturing traffic on that proxy i must start tshark in that server.</p><p>Code :</p><p>wireshark -k -i &lt;(ssh [email protected] "tshark -F pcap -w - -f 'not tcp port x'")</p><p>This is what i get in terminal:</p><p>[[email protected] Domain ~]$ wireshark -k -i &lt;(ssh [email protected] "tshark -F pcap -w - -f 'not tcp port x'")</p><p>Enter passphrase for key '/home/OSUserName/.ssh/id_rsa':</p><p>[email protected]'s password:</p><p>Permission denied, please try again.</p><p>[email protected]'s password:</p><p>Permission denied, please try again.</p><p>[email protected]'s password:</p><p>Permission denied (publickey,password).</p></div><div id="question-tags" class="tags-container tags">tshark ssh wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/28813d88f117c5dd21262285b5b83096?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anderer455&#39;s gravatar image" /><p>anderer455<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anderer455 has no accepted answers">0%</span></p></div></div><div id="comments-container-58770" class="comments-container"><span id="58771"></span><div id="comment-58771" class="comment"><div id="post-58771-score" class="comment-score"></div><div class="comment-text"><p>Fedora 25 And wireshark fully configured on main machine. (2.2.2 version)</p></div><div id="comment-58771-info" class="comment-info"><span class="comment-age">(15 Jan '17, 07:06)</span> anderer455</div></div><span id="58775"></span><div id="comment-58775" class="comment"><div id="post-58775-score" class="comment-score"></div><div class="comment-text"><p>Maybe this can help: <a href="https://wiki.wireshark.org/CaptureSetup/Pipes#Remote_Capture">https://wiki.wireshark.org/CaptureSetup/Pipes#Remote_Capture</a></p></div><div id="comment-58775-info" class="comment-info"><span class="comment-age">(15 Jan '17, 08:30)</span> Jaap ♦</div></div><span id="58778"></span><div id="comment-58778" class="comment"><div id="post-58778-score" class="comment-score"></div><div class="comment-text"><p>No this is not helping :/</p></div><div id="comment-58778-info" class="comment-info"><span class="comment-age">(15 Jan '17, 08:52)</span> anderer455</div></div><span id="58784"></span><div id="comment-58784" class="comment"><div id="post-58784-score" class="comment-score"></div><div class="comment-text"><p>Okay, I see two differences from that page: 1. The use of a password, which should either be solved through a ssh-agent or the use of a fifo, and 2. the use if dumpcap instead of tshark.</p></div><div id="comment-58784-info" class="comment-info"><span class="comment-age">(15 Jan '17, 11:44)</span> Jaap ♦</div></div></div><div id="comment-tools-58770" class="comment-tools"></div><div class="clear"></div><div id="comment-58770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


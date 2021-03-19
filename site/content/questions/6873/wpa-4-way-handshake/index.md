+++
type = "question"
title = "WPA 4-way handshake"
description = '''From this wiki page: WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless *all four* handshake packets are present for the session you&#x27;re trying to decrypt, Wireshark won&#x27;t be able to decrypt the traffic. You can use the display filter eapol to locate EAPOL packets in you...'''
date = "2011-10-12T15:39:00Z"
lastmod = "2011-10-12T15:39:00Z"
weight = 6873
keywords = [ "decryption", "wpa" ]
aliases = [ "/questions/6873" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WPA 4-way handshake](/questions/6873/wpa-4-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6873-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From <a href="http://wiki.wireshark.org/HowToDecrypt802.11">this wiki page</a>:</p><pre><code>WPA and WPA2 use keys derived from an EAPOL handshake to encrypt
traffic. Unless *all four* handshake packets are present for the
session you&#39;re trying to decrypt, Wireshark won&#39;t be able to
decrypt the traffic. You can use the display filter eapol to
locate EAPOL packets in your capture.</code></pre><p>I've noticed that it works with (1,2,4) too. Can someone please explain this?</p><h1 id="test-case">Test case</h1><p>This is the gzipped handshake (1, 2, 4) and an ecrypted <code>ARP</code> packet (SSID: <code>SSID</code>, password: <code>password</code>) in <code>base64</code> encoding:</p><pre><code>H4sICEarjU8AA2hhbmRzaGFrZS5jYXAAu3J400ImBhYGGPj/n4GhHkhfXNHr37KQgWEqAwQzMAgx
6HkAKbFWzgUMhxgZGDiYrjIwKGUqcW5g4Ldd3rcFQn5IXbWKGaiso4+RmSH+H0MngwLUZMarj4Rn
S8vInf5yfO7mgrMyr9g/Jpa9XVbRdaxH58v1fO3vDCQDkCNv7mFgWMsAwXBHMoEceQ3kSMZbDFDn
ITk1gBnJkeX/GDkRjmyccfus4BKl75HC2cnW1eXrjExNf66uYz+VGLl+snrF7j2EnHQy3JjDKPb9
3fOd9zT0TmofYZC4K8YQ8IkR6JaAT0zIJMjxtWaMmCEMdvwNnI5PYEYJYSTHM5EegqhggYbFhgsJ
9gJXy42PMx9JzYKEcFkcG0MJULYE2ZEGrZwHIMnASwc1GSw4mmH1JCCNQYEF7C7tjasVT+0/J3LP
gie59HFL+5RDIdmZ8rGMEldN5s668eb/tp8vQ+7OrT9jPj/B7425QIGJI3Pft72dLxav8BefvcGU
7+kfABxJX+SjAgAA</code></pre><p>Decode with:</p><pre><code>$ base64 -d | gunzip &gt; handshake.cap</code></pre><p>Run <code>tshark</code> to see if it correctly decrypt the <code>ARP</code> packet:</p><pre><code>$ tshark -r handshake.cap -o wlan.enable_decryption:TRUE -o wlan.wep_key1:wpa-pwd:password:SSID</code></pre><p>It should print:</p><pre><code>  1   0.000000 D-Link_a7:8e:b4 -&gt; HonHaiPr_22:09:b0 EAPOL Key
  2   0.006997 HonHaiPr_22:09:b0 -&gt; D-Link_a7:8e:b4 EAPOL Key
  3   0.038137 HonHaiPr_22:09:b0 -&gt; D-Link_a7:8e:b4 EAPOL Key
  4   0.376050 ZyxelCom_68:3a:e4 -&gt; HonHaiPr_22:09:b0 ARP 192.168.1.1 is at 00:a0:c5:68:3a:e4</code></pre></div><div id="question-tags" class="tags-container tags">decryption wpa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/f9fe811b8339fd327447c08e837c8ef3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cYrus&#39;s gravatar image" /><p>cYrus<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cYrus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '12, 02:07</p></div></div><div id="comments-container-6873" class="comments-container"><span id="10279"></span><div id="comment-10279" class="comment"><div id="post-10279-score" class="comment-score"></div><div class="comment-text"><p>Not sure if I got that right - so please comment on every guess here: afaik eapol msgs 1 and 2 are the most important ones because Anonce and Snonce are readable in there, so you can check if the given PSK is correct by calculating PTK out of A/Snonce. EAPOL msg 3 from what I remember was for supplying GTK, so this might affect decoding broadcast only, but like mentioned JUST guessing here...</p></div><div id="comment-10279-info" class="comment-info"><span class="comment-age">(19 Apr '12, 05:55)</span> Landi</div></div><span id="10477"></span><div id="comment-10477" class="comment"><div id="post-10477-score" class="comment-score"></div><div class="comment-text"><p>AFAIK you're right, the question is: "How does Wireshark really perform decryption?".</p></div><div id="comment-10477-info" class="comment-info"><span class="comment-age">(27 Apr '12, 04:37)</span> cYrus</div></div><span id="10497"></span><div id="comment-10497" class="comment"><div id="post-10497-score" class="comment-score"></div><div class="comment-text"><p>I guess that comes to "read the f%$!ing code" :D at least that's what I assume comes next for understanding how wireshark decodes the stuff</p><p>@devs: any info?</p></div><div id="comment-10497-info" class="comment-info"><span class="comment-age">(28 Apr '12, 05:16)</span> Landi</div></div><span id="10502"></span><div id="comment-10502" class="comment"><div id="post-10502-score" class="comment-score"></div><div class="comment-text"><p>Yep, I guess that's the one... :/ I've sent a message in the mailing list, still no answers.</p></div><div id="comment-10502-info" class="comment-info"><span class="comment-age">(28 Apr '12, 14:43)</span> cYrus</div></div></div><div id="comment-tools-6873" class="comment-tools"></div><div class="clear"></div><div id="comment-6873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


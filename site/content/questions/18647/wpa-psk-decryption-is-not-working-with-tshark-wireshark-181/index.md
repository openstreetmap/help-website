+++
type = "question"
title = "wpa-psk decryption is not working with tshark (wireshark 1.8.1)"
description = '''I am trying to decrypt captured wpa-psk traffic with tshark, but it&#x27;s not recognizing the option I&#x27;m trying to override. This option allows me to specify a PSK to use for decrypting. I&#x27;m using tshark 1.8.1 with windows xp. # tshark -o wlan.wep_key1:wpa-pwd:validation tshark: -o flag &quot;wlan.wep_key1:w...'''
date = "2013-02-14T23:32:00Z"
lastmod = "2013-03-24T04:47:00Z"
weight = 18647
keywords = [ "tshark" ]
aliases = [ "/questions/18647" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wpa-psk decryption is not working with tshark (wireshark 1.8.1)](/questions/18647/wpa-psk-decryption-is-not-working-with-tshark-wireshark-181)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18647-score" class="post-score" title="current number of votes">0</div><span id="post-18647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt captured wpa-psk traffic with tshark, but it's not recognizing the option I'm trying to override. This option allows me to specify a PSK to use for decrypting. I'm using tshark 1.8.1 with windows xp. # tshark -o wlan.wep_key1:wpa-pwd:validation tshark: -o flag "wlan.wep_key1:wpa-pwd:validation" specifies unknown preference. PSK decyption was working in earlier version of wireshark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/7ee68da2708ad0f94796a0d4432f1cd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joshy&#39;s gravatar image" /><p><span>Joshy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joshy has no accepted answers">0%</span></p></div></div><div id="comments-container-18647" class="comments-container"><span id="19586"></span><div id="comment-19586" class="comment"><div id="post-19586-score" class="comment-score"></div><div class="comment-text"><p>Hi. I have also problems with tshark and WPA decryption (Wireshark 1.8.2 64bit Ubuntu). I used the command tshark -r myFile.pcap -o "wlan.enable_decryption:TRUE" -o wlan.wep_key1:wpa-pwd:MyPassword:MySSID This ends in the error message: tshark: -o flag "wlan.wep_key1:wpa-pwd:MyPassword:MySSID" specifies unknown preference</p><p>If I open Wireshark, and -&gt;Edit-&gt;Preferences-&gt;Protocols-&gt;IEEE 802.11-&gt; and enable decryption and set the Key (wpa-pwd myPassword:SSID), I see the decrypted Traffic in Wireshark. What's wrong in my tshark command?</p></div><div id="comment-19586-info" class="comment-info"><span class="comment-age">(17 Mar '13, 08:24)</span> <span class="comment-user userinfo">RS2000</span></div></div><span id="19785"></span><div id="comment-19785" class="comment"><div id="post-19785-score" class="comment-score"></div><div class="comment-text"><pre><code>Version: TShark 1.6.8 (SVN Rev 42761 from /trunk-1.6)
The following command is still working:
tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154 -R &quot;eapol || smb&quot; -w q19664_eapol_smb_h2_2.pcap

Version: TShark 1.7.0 (SVN Rev 39768 from /trunk)
These commands are not working anymore:
$ tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154 -R &quot;eapol || smb&quot; -w q19664_eapol_smb_h2_2.pcap
** (tshark.exe:3768): WARNING **: C:\Documents and Settings\user\Application Data\Wireshark\preferences line 3366: No such preference &quot;wlan.wep_key1&quot; (applying your preferences once should remove this warning)
** (tshark.exe:3768): WARNING **: C:\Documents and Settings\user\Application Data\Wireshark\preferences line 3370: No such preference &quot;wlan.wep_key2&quot; (applying your preferences once should remove this warning)
tshark: -o flag &quot;wlan.wep_key1:wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154&quot; specifies unknown preference

tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-pwd:myAPretos2 -R &quot;eapol || smb&quot; -w q19664_eapol_smb_h2_2.pcap
$ tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-pwd:myAPretos2 -R &quot;eapol || smb&quot; -w q19664_eapol_smb_h2_2.pcap
** (tshark.exe:528): WARNING **: C:\Documents and Settings\user\Application Data\Wireshark\preferences line 3366: No such preference &quot;wlan.wep_key1&quot; (applying your preferences once should remove this warning)
** (tshark.exe:528): WARNING **: C:\Documents and Settings\user\Application Data\Wireshark\preferences line 3370: No such preference &quot;wlan.wep_key2&quot; (applying your preferences once should remove this warning)
tshark: -o flag &quot;wlan.wep_key1:wpa-pwd:myAPretos2&quot; specifies unknown preference

Note
The keys are stored in the &quot;80211_keys&quot; file instead of the &quot;Preferences&quot; file.
Are those warnings related to this?

Note
Version 1.6.9: the command is still working, but Wireshark 1.6.9 has another problem: [missing libxml2-2.dll](http://ask.wireshark.org/questions/13297/how-do-you-resolve-wireshark-169-libxml2-2dll-error)
</code></pre></div><div id="comment-19785-info" class="comment-info"><span class="comment-age">(24 Mar '13, 04:47)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-18647" class="comment-tools"></div><div class="clear"></div><div id="comment-18647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "Unable to decrypt the esp packets to extract SIP messages using esp_sa file"
description = '''Unable to decrypt the esp packets to extract SIP messages using esp_sa file saved in the location where the pcap file mycapture.pcap is present. esp_sa file contents: &quot;IPv6&quot;,&quot;&quot;,&quot;&quot;,&quot;*&quot;,&quot;null&quot;,&quot;0X7B632E001C303C3C22CFADBF08D6D04F&quot;,&quot;HMAC-SHA-1-96&quot;,&quot;0XF7EDFD9700F446B1A6C9596070C6EA71&quot; tshark command: tsh...'''
date = "2015-08-19T12:08:00Z"
lastmod = "2015-08-19T12:44:00Z"
weight = 45245
keywords = [ "esp_sa", "sip", "decrypt", "esp" ]
aliases = [ "/questions/45245" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt the esp packets to extract SIP messages using esp\_sa file](/questions/45245/unable-to-decrypt-the-esp-packets-to-extract-sip-messages-using-esp_sa-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45245-score" class="post-score" title="current number of votes">0</div><span id="post-45245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Unable to decrypt the esp packets to extract SIP messages using esp_sa file saved in the location where the pcap file mycapture.pcap is present. esp_sa file contents: "IPv6","<em>","</em>","*","null","0X7B632E001C303C3C22CFADBF08D6D04F","HMAC-SHA-1-96","0XF7EDFD9700F446B1A6C9596070C6EA71" tshark command: tshark -nr mycapture.pcap -o esp.enable_encryption_decode:TRUE -o esp.enable_null_encryption_decode_heuristic:TRUE -o esp.enable_authentication_check:TRUE I'm looking for way where this can be automated with the keys in esp_sa file. Looking forward for some help. Thanks, Irina</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-esp_sa" rel="tag" title="see questions tagged &#39;esp_sa&#39;">esp_sa</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '15, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/3d5d279732303c06833e3022cc6f5443?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arathika&#39;s gravatar image" /><p><span>arathika</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arathika has no accepted answers">0%</span></p></div></div><div id="comments-container-45245" class="comments-container"><span id="45247"></span><div id="comment-45247" class="comment"><div id="post-45247-score" class="comment-score"></div><div class="comment-text"><p>I'am looking to decrypt esp packets using tshark by dynamically generating the file esp_sa. Is there a tshark command that can use the keys from esp_sa file and decrypt the esp packets with having to set this through edit-&gt;preference-&gt;esp&gt;edit esp_sa's manually</p></div><div id="comment-45247-info" class="comment-info"><span class="comment-age">(19 Aug '15, 12:44)</span> <span class="comment-user userinfo">arathika</span></div></div></div><div id="comment-tools-45245" class="comment-tools"></div><div class="clear"></div><div id="comment-45245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


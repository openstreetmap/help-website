+++
type = "question"
title = "Why can&#x27;t I see any readable data in this pcap file?"
description = '''Ok so I captured a login session but I can&#x27;t see anything in wireshark, when I click &#x27;follow tcp streams&#x27; I only see &quot;random&quot; strings, but no readable content. Could someone help me out? The link is here: https://www.dropbox.com/s/d0dv99hhacqz0hv/decrypted.cap?dl=0'''
date = "2015-10-01T12:44:00Z"
lastmod = "2015-10-01T12:44:00Z"
weight = 46323
keywords = [ "sniffing", "password", "wep" ]
aliases = [ "/questions/46323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I see any readable data in this pcap file?](/questions/46323/why-cant-i-see-any-readable-data-in-this-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok so I captured a login session but I can't see anything in wireshark, when I click 'follow tcp streams' I only see "random" strings, but no readable content. Could someone help me out? The link is here:</p><p><a href="https://www.dropbox.com/s/d0dv99hhacqz0hv/decrypted.cap?dl=0">https://www.dropbox.com/s/d0dv99hhacqz0hv/decrypted.cap?dl=0</a></p></div><div id="question-tags" class="tags-container tags">sniffing password wep</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '15, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/9ac6cd419014092f44d21ec71233b1e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shad0w125&#39;s gravatar image" /><p>shad0w125<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shad0w125 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '15, 15:49</p></div></div><div id="comments-container-46323" class="comments-container"><span id="46326"></span><div id="comment-46326" class="comment"><div id="post-46326-score" class="comment-score"></div><div class="comment-text"><p>Which stream ID do you mean?</p></div><div id="comment-46326-info" class="comment-info"><span class="comment-age">(01 Oct '15, 12:56)</span> Christian_R</div></div><span id="46327"></span><div id="comment-46327" class="comment"><div id="post-46327-score" class="comment-score"></div><div class="comment-text"><p>I mean almost all of them,I've captured a login session but the only thing I could find so far was data about the web browser in use.</p></div><div id="comment-46327-info" class="comment-info"><span class="comment-age">(01 Oct '15, 13:03)</span> shad0w125</div></div><span id="46328"></span><div id="comment-46328" class="comment"><div id="post-46328-score" class="comment-score"></div><div class="comment-text"><p>What do you expect to see? Network data is not always transmitted in a human readable format.</p></div><div id="comment-46328-info" class="comment-info"><span class="comment-age">(01 Oct '15, 13:06)</span> Jim Aragon</div></div><span id="46329"></span><div id="comment-46329" class="comment"><div id="post-46329-score" class="comment-score"></div><div class="comment-text"><p>Well I've captured a login session with an email and password, the pcap file was encrypted with the old WEP standard, I then decrypted but now I can't find the login session. What I find weird is that the other pcap files were fully readable, how could I decypher these packets?</p></div><div id="comment-46329-info" class="comment-info"><span class="comment-age">(01 Oct '15, 13:09)</span> shad0w125</div></div><span id="46342"></span><div id="comment-46342" class="comment"><div id="post-46342-score" class="comment-score"></div><div class="comment-text"><p>Layered security. WEP just handles the lowest (datalink) layer, while SSL rides on the transport layer. You talk about 'other pcap files' which we can't see?</p></div><div id="comment-46342-info" class="comment-info"><span class="comment-age">(02 Oct '15, 08:41)</span> Jaap ♦</div></div><span id="46347"></span><div id="comment-46347" class="comment not_top_scorer"><div id="post-46347-score" class="comment-score"></div><div class="comment-text"><p>So the traffic is still encrypted with SSL after decrypting WEP? Nevermind the other pcap files I mentioned, they were captured from another network, I don't even know why I mentioned it</p></div><div id="comment-46347-info" class="comment-info"><span class="comment-age">(02 Oct '15, 15:47)</span> shad0w125</div></div></div><div id="comment-tools-46323" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-46323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


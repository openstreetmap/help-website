+++
type = "question"
title = "occurrence=f/a/l  all give same output"
description = '''I want to extract some fields from a pcap file, i have written followingcode for it tshark -r file -T fields -E separator=, -e frame.time -e wlan.sa -E occurrence=f &amp;gt; output.csv  but it gives repetitive result,changing occurences a and l also gives same result. Why isnt this field having no effec...'''
date = "2016-08-14T22:55:00Z"
lastmod = "2016-08-14T22:55:00Z"
weight = 54806
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/54806" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [occurrence=f/a/l all give same output](/questions/54806/occurrencefal-all-give-same-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54806-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to extract some fields from a pcap file, i have written followingcode for it</p><p>tshark -r file -T fields -E separator=, -e frame.time -e wlan.sa -E occurrence=f &gt; output.csv</p><p>but it gives repetitive result,changing occurences a and l also gives same result. Why isnt this field having no effect</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '16, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/557d426153aa6950b4ae3541a97ab03d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tatsugot&#39;s gravatar image" /><p>tatsugot<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tatsugot has no accepted answers">0%</span></p></div></div><div id="comments-container-54806" class="comments-container"><span id="54807"></span><div id="comment-54807" class="comment"><div id="post-54807-score" class="comment-score"></div><div class="comment-text"><p>By "repetitive result" do you mean you get more than one occurrence of the time stamp. or source address, on each line of output?</p></div><div id="comment-54807-info" class="comment-info"><span class="comment-age">(14 Aug '16, 23:59)</span> Guy Harris ♦♦</div></div><span id="54808"></span><div id="comment-54808" class="comment"><div id="post-54808-score" class="comment-score">1</div><div class="comment-text"><p>I'd guess it is a misunderstanding. The <code>-E occurrence</code> parameter controls how several occurrences of the same protocol field <strong>in a single frame</strong> are treated. As <code>frame.time</code> and normally also <code>wlan.sa</code> exist just once in each frame, I'd suppose that you want to see the timestamp of the first occurrence of each <code>wlan.sa</code> MAC address in the capture. But to do that, you'll need a script - tshark cannot do this directly.</p></div><div id="comment-54808-info" class="comment-info"><span class="comment-age">(15 Aug '16, 00:51)</span> sindy</div></div><span id="54838"></span><div id="comment-54838" class="comment"><div id="post-54838-score" class="comment-score"></div><div class="comment-text"><p>My guess is that <em>but it gives repetitive result</em> was meant to say, <em>but it gives the same result</em>.</p><p>If there's only one occurrence of a field within a packet, then the first occurrence is the same as the last occurrence is the same as all occurrences - you get the single occurrence in all 3 cases.</p></div><div id="comment-54838-info" class="comment-info"><span class="comment-age">(15 Aug '16, 10:00)</span> cmaynard ♦♦</div></div><span id="55288"></span><div id="comment-55288" class="comment"><div id="post-55288-score" class="comment-score"></div><div class="comment-text"><p>Sorry, It was my mistake. The file had only one field.</p></div><div id="comment-55288-info" class="comment-info"><span class="comment-age">(02 Sep '16, 05:50)</span> tatsugot</div></div></div><div id="comment-tools-54806" class="comment-tools"></div><div class="clear"></div><div id="comment-54806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


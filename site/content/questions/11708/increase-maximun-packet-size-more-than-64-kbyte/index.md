+++
type = "question"
title = "Increase maximun packet size (more than 64 Kbyte)"
description = '''Hello to all I try to increase the maximun packet size that Wireshark can read in order to support packets up to 16 Mbyte (or even more up to 256 Mbyte). I already changed the WTAP_MAX_PACKET_SIZE to 32 * 1024 * 1024 in wireshark/wiretap/wiretap.h and recompiled succesfully the Wireshark. I also suc...'''
date = "2012-06-06T00:13:00Z"
lastmod = "2013-06-14T03:04:00Z"
weight = 11708
keywords = [ "kbyte", "larger", "64", "than", "packet" ]
aliases = [ "/questions/11708" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Increase maximun packet size (more than 64 Kbyte)](/questions/11708/increase-maximun-packet-size-more-than-64-kbyte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11708-score" class="post-score" title="current number of votes">0</div><span id="post-11708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello to all</p><p>I try to increase the maximun packet size that Wireshark can read in order to support packets up to 16 Mbyte (or even more up to 256 Mbyte). I already changed the WTAP_MAX_PACKET_SIZE to 32 * 1024 * 1024 in wireshark/wiretap/wiretap.h and recompiled succesfully the Wireshark. I also succesfully read a PCAP file where each packet is 16 Mbyte each in command line with tshark -r file.pcap.</p><p>My problem is that I cannot read the same file in the Wireshark's GUI. When I try to open the same file in GUI, the GUI is stop working. Even if I try to capture my Ethernet card the dumpcap is stop working and the message "Child dumpcap process died: Stack overflow" appears.</p><p>Any suggestion of how to succesfully support packets larger than 64 Kbyte in GUI?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kbyte" rel="tag" title="see questions tagged &#39;kbyte&#39;">kbyte</span> <span class="post-tag tag-link-larger" rel="tag" title="see questions tagged &#39;larger&#39;">larger</span> <span class="post-tag tag-link-64" rel="tag" title="see questions tagged &#39;64&#39;">64</span> <span class="post-tag tag-link-than" rel="tag" title="see questions tagged &#39;than&#39;">than</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/a316969e99cc919815d47ae1fc022a55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andapo&#39;s gravatar image" /><p><span>andapo</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andapo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '13, 00:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-11708" class="comments-container"><span id="22047"></span><div id="comment-22047" class="comment"><div id="post-22047-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any suggestion of how to succesfully support packets larger than 64 Kbyte in GUI?</p></blockquote><p>Just a question. Where do you actually see (single) <strong>packets</strong> with a size of <strong>256 MByte</strong>?</p></div><div id="comment-22047-info" class="comment-info"><span class="comment-age">(14 Jun '13, 03:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11708" class="comment-tools"></div><div class="clear"></div><div id="comment-11708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


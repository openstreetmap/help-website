+++
type = "question"
title = "Period [.] missing after ENUM/DNS query in wireshark"
description = '''I am attaching a ENUM/DNS Trace which we have captured over the wire in the DNS Protocol section,I am sending this following query No. Time Source Destination Protocol Info  1 0.000000 172.17.219.68 10.230.35.248 DNS Standard query NAPTR 6.1.0.0.1.1.3.3.4.0.1.8.e164enum.net  Frame 1: 107 bytes on wi...'''
date = "2016-11-12T02:40:00Z"
lastmod = "2016-11-16T05:36:00Z"
weight = 57333
keywords = [ "dns" ]
aliases = [ "/questions/57333" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Period \[.\] missing after ENUM/DNS query in wireshark](/questions/57333/period-missing-after-enumdns-query-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57333-score" class="post-score" title="current number of votes">0</div><span id="post-57333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attaching a ENUM/DNS Trace which we have captured over the wire</p><p>in the DNS Protocol section,I am sending this following query</p><pre><code>No.     Time        Source                Destination           Protocol Info
      1 0.000000    172.17.219.68         10.230.35.248         DNS      Standard query NAPTR 6.1.0.0.1.1.3.3.4.0.1.8.e164enum.net

Frame 1: 107 bytes on wire (856 bits), 107 bytes captured (856 bits)
Ethernet II, Src: Cisco_4c:36:17 (00:1e:4a:4c:36:17), Dst: 40:a8:f0:26:c7:08 (40:a8:f0:26:c7:08)
Internet Protocol, Src: 172.17.219.68 (172.17.219.68), Dst: 10.230.35.248 (10.230.35.248)
User Datagram Protocol, Src Port: 14126 (14126), Dst Port: domain (53)
Domain Name System (query)
    [Response In: 2]
    Transaction ID: 0x3be5
    Flags: 0x0100 (Standard query)
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 1
    Queries
        6.1.0.0.1.1.3.3.4.0.1.8.e164enum.net: type NAPTR, class IN
            Name: 6.1.0.0.1.1.3.3.4.0.1.8.e164enum.net
            Type: NAPTR (Naming authority pointer)
            Class: IN (0x0001)
    Additional records

0000  40 a8 f0 26 c7 08 00 1e 4a 4c 36 17 08 00 45 00   @..&amp;....JL6...E.
0010  00 5d cd 1f 40 00 ff 11 f8 3b ac 11 db 44 0a e6   .][email protected];...D..
0020  23 f8 37 2e 00 35 00 49 70 ee 3b e5 01 00 00 01   #.7..5.Ip.;.....
0030  00 00 00 00 00 01 01 36 01 31 01 30 01 30 01 31   .......6.1.0.0.1
0040  01 31 01 33 01 33 01 34 01 30 01 31 01 38 08 65   .1.3.3.4.0.1.8.e
0050  31 36 34 65 6e 75 6d 03 6e 65 74 00 00 23 00 01   164enum.net..#..
0060  00 00 29 10 00 00 00 80 00 00 00                  ..)........</code></pre><p>Our Application Logs show a . [period] after e164enum.net as e164enum.net. But wireshark is removing the . after net and displaying only "e164enum.net". Why is wireshark showing Like this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '16, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/1f20ad75c149967bea2416b13ecf716a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="h4harshith&#39;s gravatar image" /><p><span>h4harshith</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="h4harshith has no accepted answers">0%</span></p></div></div><div id="comments-container-57333" class="comments-container"></div><div id="comment-tools-57333" class="comment-tools"></div><div class="clear"></div><div id="comment-57333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57336"></span>

<div id="answer-container-57336" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57336-score" class="post-score" title="current number of votes">3</div><span id="post-57336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="h4harshith has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In a DNS request, the name is represented by a series of labels, where each label is preceded with the length of the label. The final label has length 0. The dot is actually not part of the name, it is just a way of representing the separation of the labels (just like the dot in an IP address is to show the separation between the octets).</p><p>In representating the FQDN, the dot in the end signifies that the name should be read as an absolute name (ie, no domain suffices should be applied anymore), while a name without a dot could be extended with a search domain. This is done on the system where the DNS lookup is performed, however, in the DNS request towards the server the search domain is already added and the name is considered an absolute name. Therefor the final dot is omitted in the DNS request.</p><p>Wireshark dissects the data as is and therefor a final dot is not displayed as it was not transmitted over the wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '16, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57336" class="comments-container"><span id="57419"></span><div id="comment-57419" class="comment"><div id="post-57419-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for your helpful inputs. Upvoted</p></div><div id="comment-57419-info" class="comment-info"><span class="comment-age">(16 Nov '16, 05:36)</span> <span class="comment-user userinfo">h4harshith</span></div></div></div><div id="comment-tools-57336" class="comment-tools"></div><div class="clear"></div><div id="comment-57336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57335"></span>

<div id="answer-container-57335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57335-score" class="post-score" title="current number of votes">3</div><span id="post-57335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is doing this as that's exactly what is transmitted on the wire, see the hex bytes display for confirmation:</p><pre><code>0030  00 00 00 00 00 01 01 36 01 31 01 30 01 30 01 31   .......6.1.0.0.1
0040  01 31 01 33 01 33 01 34 01 30 01 31 01 38 08 65   .1.3.3.4.0.1.8.e
0050  31 36 34 65 6e 75 6d 03 6e 65 74 00 00 23 00 01   164enum.net..#..
                                       ^^</code></pre><p>Note the byte after the "t" is 0x00, there is no period.</p><p>Your application software must be creating the "." suffix itself.</p><p>You can also see the hex bytes corresponding to a field in Wireshark by clicking the field in the packet details pane, the hex bytes pane will then highlight the respective bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '16, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57335" class="comments-container"><span id="57420"></span><div id="comment-57420" class="comment"><div id="post-57420-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for your helpful inputs. Upvoted</p></div><div id="comment-57420-info" class="comment-info"><span class="comment-age">(16 Nov '16, 05:36)</span> <span class="comment-user userinfo">h4harshith</span></div></div></div><div id="comment-tools-57335" class="comment-tools"></div><div class="clear"></div><div id="comment-57335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


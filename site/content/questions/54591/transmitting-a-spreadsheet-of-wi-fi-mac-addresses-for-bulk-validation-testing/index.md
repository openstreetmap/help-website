+++
type = "question"
title = "Transmitting a spreadsheet of Wi-Fi MAC addresses for bulk validation testing"
description = '''Looking for a way to take a spreadsheet containing 100 (or more) randomized Wi-Fi MAC addresses and transmit them over Wi-fi using a pre-determined interval, (1 second, 5 seconds etc.) then determine the accuracy of a reciever in detecting the transmitted MAC addresses. Have access to Wireshark and ...'''
date = "2016-08-04T21:00:00Z"
lastmod = "2016-08-05T08:36:00Z"
weight = 54591
keywords = [ "transmits", "wifi", "mac-address", "validation", "retransmission" ]
aliases = [ "/questions/54591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Transmitting a spreadsheet of Wi-Fi MAC addresses for bulk validation testing](/questions/54591/transmitting-a-spreadsheet-of-wi-fi-mac-addresses-for-bulk-validation-testing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54591-score" class="post-score" title="current number of votes">0</div><span id="post-54591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking for a way to take a spreadsheet containing 100 (or more) randomized Wi-Fi MAC addresses and transmit them over Wi-fi using a pre-determined interval, (1 second, 5 seconds etc.) then determine the accuracy of a reciever in detecting the transmitted MAC addresses. Have access to Wireshark and Linux Machines. System and methodology got detecting the signals and archiving them is established. It is the randomized creation and transmission part that is creating difficulties. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-transmits" rel="tag" title="see questions tagged &#39;transmits&#39;">transmits</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span> <span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '16, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/8d202a8371e364236f3257607101122e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="t1mcca11&#39;s gravatar image" /><p><span>t1mcca11</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="t1mcca11 has no accepted answers">0%</span></p></div></div><div id="comments-container-54591" class="comments-container"><span id="54592"></span><div id="comment-54592" class="comment"><div id="post-54592-score" class="comment-score"></div><div class="comment-text"><p>Can you be more specific regarding the required scenario? In particular, do you want to transmit frames with these addresses as source addresses, destination addresses, transmitter addresses, receiver addresses (or a combination thereof)? Source and destination should be fairly simple to imitate, transmitter almost impossible and receiver would likely require a patched driver (I consider unlikely that a stock driver would be willing to send a frame to a non-associated receiver).</p></div><div id="comment-54592-info" class="comment-info"><span class="comment-age">(04 Aug '16, 23:07)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54617"></span><div id="comment-54617" class="comment"><div id="post-54617-score" class="comment-score"></div><div class="comment-text"><p>we are trying to validate hardware used to sample wifi MAC addresses and calculate travel times from point A to point B. I believe we just need the Source MAC address to upload to a database from multiple simulated locations to validate the underlying travel time analytics. Bob's answer below will get us moving in the right direection. We will have one transmitter or packet injection source, wireshark and our device. The detected MAC addresses will be compared between the Wireshark database and our devices database for detection percentage and matching validation.</p></div><div id="comment-54617-info" class="comment-info"><span class="comment-age">(05 Aug '16, 08:36)</span> <span class="comment-user userinfo">t1mcca11</span></div></div></div><div id="comment-tools-54591" class="comment-tools"></div><div class="clear"></div><div id="comment-54591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54607"></span>

<div id="answer-container-54607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54607-score" class="post-score" title="current number of votes">0</div><span id="post-54607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is an interesting test scenario so I agree with <span><span>@sindy</span></span>: what are you really trying to do here? This also isn't really a Wireshark question, though the capture and analysis could be.</p><p>Packet injection is possible with some wifi cards, though I find it even trickier than just capturing traffic. A couple of places to get started with WiFi injection are:</p><p><a href="http://www.aircrack-ng.org/">http://www.aircrack-ng.org/</a></p><p>and in particular</p><p><a href="http://www.aircrack-ng.org/doku.php?id=aireplay-ng">http://www.aircrack-ng.org/doku.php?id=aireplay-ng</a></p><p>I know these tools can work to do packet injection on WiFi. The aireplay tool has an injection test mode that you will certainly want to try first as not all WiFi adapters will do injection properly. Even if they do injection, there is no guarantee that you have control over all the fields. I found it best to have a selection of adapters, and depending on exactly what I want to inject, I try the various adapters and see how the data 'on the wire' (really in the air...) behaves. Sometimes I can get what I need, but not always.</p><p>Generally, faking MAC addresses seems to be pretty straightforward on many adapters. Adjusting things like NAV timer, Association ID, or even datarate can be much harder. Perhaps, though, if you only need to vary MAC addresses you have a good chance when the adapter is in monitor mode.</p><p>Airtun-ng (part of this same suite) is another tool that can inject. I get different results, sometimes, than with aireplay, so try both to verify results. Having good capture capability for this is critical to validate you can do proper injection.</p><p>For the overall problem, once you prove to yourself you can actually inject, is to automate. My plan of attack would be to do a perl or python script on Linux to create the random MAC addresses and then use a simple loop to call the aireplay (or whatever) executable, with arguments changing at each loop iteration. Here is an example command to inject a pcap file on wireless - for this test, I hand-edit the hex bytes in a pcap file to get the packet exactly as I want, then call the executable:</p><p>aireplay-ng -2 -v 10 -u 1 -w 0 -m 10 -n 100 -h 00:2A:BF:44:DC:51 -r output1.cap mon0</p><p>If I need to send multiple packets, I would look for a CLI option to keep sending, or script up a loop and control the timing that way (i.e. number of iterations, period between frames, etc.) Manipulating the hex bytes in perl or python should be straightforward, so creating an 'on demand' pcap file to use to inject and then injecting it is the task at hand, adjusting the pcap file at each loop iteration through your random mac address list, which could be read from a file or created on demand by the script. There are also some tools for manipulating pcap files that may or may not be useful here (packetforge, etc). As <span><span>@sindy</span></span> notes, change which ever address field (you have an option of three or four...) of the chosen 802.11 frame type - Data, QoS Data, Null, QoS-Null, lots of options.</p><p>Others with more programming background will likely have better plans on how to automate once you have the actually injection piece working.<br />
</p><p>I have this notion that OmniPeek will inject WiFI packets, but have never done it so can't be sure. You can check there for a possible Windows solution at www.savvius.com.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-54607" class="comments-container"><span id="54615"></span><div id="comment-54615" class="comment"><div id="post-54615-score" class="comment-score"></div><div class="comment-text"><p>Great info. Will be working on this over the weekend.</p></div><div id="comment-54615-info" class="comment-info"><span class="comment-age">(05 Aug '16, 08:32)</span> <span class="comment-user userinfo">t1mcca11</span></div></div></div><div id="comment-tools-54607" class="comment-tools"></div><div class="clear"></div><div id="comment-54607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "I lose data when filtering in a reassembled PDU"
description = '''Hi all! I&#x27;m trying to filter out a real large pcap file using tshark (I don&#x27;t want to load that really large file in Wireshark) into a new pcap file. I&#x27;m filtering by rating group in Diameter but when it applies the filter over a reassembled PDU it seems that it only filters one of the segments of t...'''
date = "2016-02-18T20:52:00Z"
lastmod = "2016-02-19T06:12:00Z"
weight = 50323
keywords = [ "filter", "reassembled", "pdu", "tshark" ]
aliases = [ "/questions/50323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I lose data when filtering in a reassembled PDU](/questions/50323/i-lose-data-when-filtering-in-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all!</p><p>I'm trying to filter out a real large pcap file using tshark (I don't want to load that really large file in Wireshark) into a new pcap file. I'm filtering by rating group in Diameter but when it applies the filter over a reassembled PDU it seems that it only filters one of the segments of that PDU because when I open the new file, I find that in those frames belonging to reassembled PDU I only get Data over TCP instead of Diameter. Do you know how can I do to be able to extract all the segments which belong to the PDUs that match the filter?</p><p>For example when I filter in the filter tab I don't have the problem but when I extract the frames it found to a new file then I have this data problem :(</p><p>Thanks all in advance!</p><p>Regards, JC</p></div><div id="question-tags" class="tags-container tags">filter reassembled pdu tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 20:52</strong></p><img src="https://secure.gravatar.com/avatar/13de941b5a89e568d71291549ef1db1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JCuadri&#39;s gravatar image" /><p>JCuadri<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JCuadri has no accepted answers">0%</span></p></div></div><div id="comments-container-50323" class="comments-container"><span id="50324"></span><div id="comment-50324" class="comment"><div id="post-50324-score" class="comment-score"></div><div class="comment-text"><p>What version of Ws are you using? This was a problem in some earlier version. I don't remember when it got fixed but it should work in 1.12 and later.</p></div><div id="comment-50324-info" class="comment-info"><span class="comment-age">(18 Feb '16, 21:43)</span> Anders ♦</div></div><span id="50356"></span><div id="comment-50356" class="comment"><div id="post-50356-score" class="comment-score"></div><div class="comment-text"><p>I'm using 1.12.1, I'll try the "2 pass" solution using tshark and I'll tell you the results.</p><p>Thanks!</p></div><div id="comment-50356-info" class="comment-info"><span class="comment-age">(19 Feb '16, 13:34)</span> JCuadri</div></div></div><div id="comment-tools-50323" class="comment-tools"></div><div class="clear"></div><div id="comment-50323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50339"></span>

<div id="answer-container-50339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50339-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To get tshark to save "dependent" frames (i.e., frames that are required to properly dissect another frame due to, for example, reassembly) you need to give tshark the "-2" option in addition to the display filter.</p><p>Think of it this way: normally tshark makes a single pass through the capture file. In the case of reassembly if, for examples, frames 5, 7, and 9 are reassembled into a single upper-layer PDU then tshark won't know that it needs to display (or save) frames 5 and 7 until it's gotten to frame 9, finished the reassembly, and found that frame 9 passes the display filter. By enabling 2 passes tshark can see frames 5 and 7 again this time with the knowledge that they need to be displayed/saved (since they are required for frame 9 to pass the display filter).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '16, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50339" class="comments-container"><span id="50357"></span><div id="comment-50357" class="comment"><div id="post-50357-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff, I'll try that and will share my results.</p><p>Regards JC</p></div><div id="comment-50357-info" class="comment-info"><span class="comment-age">(19 Feb '16, 13:35)</span> JCuadri</div></div><span id="50364"></span><div id="comment-50364" class="comment"><div id="post-50364-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff, I still have a problem. Now it takes all the frames (the ones that pass the filter and the ones that need to be considered for the reassembly of one PDU which passes the filter) into the new file. The problem is that in the new file I've got them separated and Wireshark does not assemble them.</p><p>For example I've got in my original file frames 548 and 558 which parts of them are reassembled to create my Diameter protocol in frame 558. When I pass the filter and create a new file (either with "2-pass" tshark or with display filter in graphic interface) those frames are separated in the new file and I can't read Diameter because for Wireshark separated that data doesn't mean anything. I've made a detailed analysis and the problem is that frame 548 depends also on frame 540 and frame 540 depends on frame 520, the problem is that the filter doesn't take those last frames... :( is it a bug or I can do something to solve this? One frame which passes the filter depends on other and this last one on other and like that for five or six times...</p></div><div id="comment-50364-info" class="comment-info"><span class="comment-age">(19 Feb '16, 21:10)</span> JCuadri</div></div><span id="50412"></span><div id="comment-50412" class="comment"><div id="post-50412-score" class="comment-score"></div><div class="comment-text"><p>Ohhhh... This is TCP isn't it?</p><p>I'm guessing that, in your example, frame 548 does not <em>start</em> a Diameter PDU (which is then completed in frame 558) but rather frame 548 contains, for example, the end of a PDU and then the start of a new one (which is finished in frame 558)?</p><p>The attachment to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11144">bug 11144</a> shows the same behavior.</p><p>With TCP the "dependent frame" stuff will only really work when there's a single frame on which the dissected (passed the display filter) frame depends. IIRC I was pretty happy just to get that much working. :-)</p><p>And frankly I don't really see a way to get it to work without also including earlier upper-layer PDUs that didn't pass the display filter.</p><p>I think to solve your use case you'd really need to use the "export PDUs to file" functionality (which may not be present in 1.12 and is almost certainly not available in tshark--maybe it should be).</p></div><div id="comment-50412-info" class="comment-info"><span class="comment-age">(22 Feb '16, 10:24)</span> JeffMorriss ♦</div></div><span id="50416"></span><div id="comment-50416" class="comment"><div id="post-50416-score" class="comment-score"></div><div class="comment-text"><p>I think we have unfinished code to add it to TShark in gerrit.</p></div><div id="comment-50416-info" class="comment-info"><span class="comment-age">(22 Feb '16, 12:21)</span> Anders ♦</div></div></div><div id="comment-tools-50339" class="comment-tools"></div><div class="clear"></div><div id="comment-50339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


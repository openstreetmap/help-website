+++
type = "question"
title = "Continuation or non-HTTP traffic won&#x27;t produce HTTP"
description = '''EDIT2: I made another capture session and uploaded it to cloudshark.org The GET request for which there is no HTTP response is frame 364 http://cloudshark.org/captures/c36979d903e0 Then I rearranged the frames in this sequence: ...-364-367-365-368-371-369-372-... I removed frames 366 &amp;amp; 370. Here...'''
date = "2013-07-19T07:26:00Z"
lastmod = "2013-07-20T09:43:00Z"
weight = 23151
keywords = [ "continuation", "google", "non-http" ]
aliases = [ "/questions/23151" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Continuation or non-HTTP traffic won't produce HTTP](/questions/23151/continuation-or-non-http-traffic-wont-produce-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23151-score" class="post-score" title="current number of votes">0</div><span id="post-23151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>EDIT2:</strong><br />
I made another capture session and uploaded it to cloudshark.org<br />
The GET request for which there is no HTTP response is frame 364<br />
<a href="http://cloudshark.org/captures/c36979d903e0">http://cloudshark.org/captures/c36979d903e0</a></p><p>Then I rearranged the frames in this sequence: ...-364-367-365-368-371-369-372-...<br />
I removed frames 366 &amp; 370. Here's the result:<br />
<a href="http://cloudshark.org/captures/5003ae96ae6b">http://cloudshark.org/captures/5003ae96ae6b</a></p><p>Both captures need SSL keys:<br />
<a href="http://pastebin.com/DMcFKW2p">http://pastebin.com/DMcFKW2p</a><br />
<br />
<br />
</p><p><strong>EDIT1:</strong><br />
Following up on SYN-bit's response, I rearranged the out-of-order packets using editcap and mergecap, but the "continuation" issue still persists.<br />
<a href="http://imgur.com/NpiXqXw">http://imgur.com/NpiXqXw</a><br />
Notice the 5 packets 365-369 are not in chronological order as the result of re-arranging.<br />
I applied all Landi's suggestions to this new pcap file, to no avail.<br />
</p><p>The "continuation" still continues to the end of the capture file. Before I interrupted the capture, the last frame with "continuation" had TCP relative Seq. on 26024, which means there was roughly 26K worth of data from the server. And yet, no HTML was dissected.<br />
<strong>END OF EDIT1</strong><br />
<br />
<br />
<br />
</p><p>I'm doing a simple action:<br />
With wireshark running,<br />
I go to <a href="https://www.google.com">https://www.google.com</a> and then click "Blogger" in the upper bar.</p><p>I'm expecting to see in wireshark: HTTP/1.1 200 OK (html/text) for the page that shows up in the browser when I press "Blogger".<br />
But all I see in wireshark is that right after my GET request for that "Blogger page", I only get "Continuation or non-HTTP traffic".<br />
After that wireshark shows that the browser starts GETing the PNGs and GIFs contained in the "Blogger page" and wireshark successfully recognizes them as PNGs and GIFs.<br />
But wireshark <strong>won't dissect the very first HTML page</strong>.</p><p>P.S. I'm using Firefox with SSLKEYLOGFILE and wireshark successfully decrypts SSL.</p><p>P.P.S Here is the relevant screenshot:<br />
<a href="http://imgur.com/plp6SRT">http://imgur.com/plp6SRT</a><br />
Notice the GET request in frame 708<br />
And the GET request in frame 732, which is a PNG linked to from the HTML file that wireshark couldn't dissect</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-continuation" rel="tag" title="see questions tagged &#39;continuation&#39;">continuation</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-non-http" rel="tag" title="see questions tagged &#39;non-http&#39;">non-http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '13, 13:19</strong> </span></p></div></div><div id="comments-container-23151" class="comments-container"></div><div id="comment-tools-23151" class="comment-tools"></div><div class="clear"></div><div id="comment-23151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23157"></span>

<div id="answer-container-23157" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23157-score" class="post-score" title="current number of votes">3</div><span id="post-23157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dansmith has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>THe problem is that the first segment of the HTTP response is received out-of-order. Since re-assembly is being initiated in the first frame that wireshark sees, it is not able to determine how to re-assemble this response. There are a couple of related bug reports on bugzilla:</p><ul><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3389">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3389</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4727">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4727</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5971">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5971</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8694">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8694</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-23157" class="comments-container"><span id="23161"></span><div id="comment-23161" class="comment"><div id="post-23161-score" class="comment-score"></div><div class="comment-text"><p>SYN-bit, any ideas if the patch in Bug 5971 can be adapted to the current version of wireshark? I could do it myself. I just need a confirmation that the code hasn't changed too drastically since 2 years ago when the patch was submitted.</p></div><div id="comment-23161-info" class="comment-info"><span class="comment-age">(19 Jul '13, 08:39)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23166"></span><div id="comment-23166" class="comment"><div id="post-23166-score" class="comment-score"></div><div class="comment-text"><p>You could just try to apply the patch and see what happens.</p></div><div id="comment-23166-info" class="comment-info"><span class="comment-age">(19 Jul '13, 09:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="23167"></span><div id="comment-23167" class="comment"><div id="post-23167-score" class="comment-score"></div><div class="comment-text"><p>Sorry to unmark your response as accepted, but I rearranged the packets and my initial issue persists</p></div><div id="comment-23167-info" class="comment-info"><span class="comment-age">(19 Jul '13, 10:06)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23171"></span><div id="comment-23171" class="comment"><div id="post-23171-score" class="comment-score"></div><div class="comment-text"><p>No worries. Do the packets contain sensitive data? If not, could you upload the faulty session to www.cloudshark.org and post the link here (together with the SSL session key for that particular SSL session)?</p></div><div id="comment-23171-info" class="comment-info"><span class="comment-age">(19 Jul '13, 11:43)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="23181"></span><div id="comment-23181" class="comment"><div id="post-23181-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I updated my OP with relevant cloudshark links.</p></div><div id="comment-23181-info" class="comment-info"><span class="comment-age">(19 Jul '13, 13:21)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23191"></span><div id="comment-23191" class="comment not_top_scorer"><div id="post-23191-score" class="comment-score"></div><div class="comment-text"><p>see my edited answer</p></div><div id="comment-23191-info" class="comment-info"><span class="comment-age">(20 Jul '13, 04:21)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="23199"></span><div id="comment-23199" class="comment not_top_scorer"><div id="post-23199-score" class="comment-score"></div><div class="comment-text"><p>In the rearranged capture file I can finally see my HTML in frame 406.</p></div><div id="comment-23199-info" class="comment-info"><span class="comment-age">(20 Jul '13, 09:43)</span> <span class="comment-user userinfo">dansmith</span></div></div></div><div id="comment-tools-23157" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-23157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23152"></span>

<div id="answer-container-23152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23152-score" class="post-score" title="current number of votes">0</div><span id="post-23152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>EDIT</strong></p><p>I downloaded your newcap trace and I perfectly see the HTTP Response code like expected</p><p>See <a href="http://imgur.com/Hnjhr6r">http://imgur.com/Hnjhr6r</a></p><p>Like said - be sure to turn off Reassembly then you'll see the return code right after the GET in frame 365, otherwise it will appear in frame 406. Mind to EITHER turn reassambly completely ON (TCP plus both settings inside SSL prefs) of OFF (again TCP plus both settings in SSL Prefs)</p><p>&lt;&lt;&lt; end of edit &gt;&gt;&gt;</p><p>It does but you have TCP segment reassembly turned on by default which is why wireshark waits until the whole data block is successfully transmitted before dissecting it as a whole.</p><p>Just turn of TCP stream reassembly in the TCP protocol prererences and you're fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '13, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '13, 04:21</strong> </span></p></div></div><div id="comments-container-23152" class="comments-container"><span id="23154"></span><div id="comment-23154" class="comment"><div id="post-23154-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately your suggestion didn't work. Right clicking a TCP frame-&gt;Protocol Preferences-&gt; unchecking Allow subdissector to reassemble TCP streams followed by screen reload didn't produce new HTTP OK's</p></div><div id="comment-23154-info" class="comment-info"><span class="comment-age">(19 Jul '13, 08:01)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23155"></span><div id="comment-23155" class="comment"><div id="post-23155-score" class="comment-score"></div><div class="comment-text"><p>could you please try filtering for a single TCP Session by right-clicking a GET request where you don't see the HTTP OK and then selecting Conversation Filter -&gt; TCP and check again</p></div><div id="comment-23155-info" class="comment-info"><span class="comment-age">(19 Jul '13, 08:12)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="23159"></span><div id="comment-23159" class="comment"><div id="post-23159-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, Conversation Filter didn't help either</p></div><div id="comment-23159-info" class="comment-info"><span class="comment-age">(19 Jul '13, 08:36)</span> <span class="comment-user userinfo">dansmith</span></div></div></div><div id="comment-tools-23152" class="comment-tools"></div><div class="clear"></div><div id="comment-23152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23195"></span>

<div id="answer-container-23195" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23195-score" class="post-score" title="current number of votes">0</div><span id="post-23195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After amalgamating SYN-bit's and Landi's answers, I realized that:</p><p>We've got 3 relevant preferences:<br />
1. Allow subdissector to reassemble TCP streams<br />
2. Reassemble SSL records spanning multiple TCP segments<br />
3. Reassemble SSL Application Data spanning multiple SSL records<br />
</p><p>I tried multiple combination of the 3 switches. In order to see "HTTP/1.1 200 OK [Unreassembled Packet]" in frame 365 of the re-arranged capture, one only needs to disable 3 (whether 1 and/or 2 is on/off doesn't matter)</p><p>But the issue remains - wireshark still won't dissect the HTML file from the chunked HTTP frames. I guess it is because wireshark expects a final chunk of size 0, but <strong>google never sends the chunk with size 0</strong>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '13, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div></div><div id="comments-container-23195" class="comments-container"><span id="23196"></span><div id="comment-23196" class="comment"><div id="post-23196-score" class="comment-score"></div><div class="comment-text"><p>what exactly do you mean by "won't dissect" what are you trying to accomplish?? Sorry I don't get it... like in my screen shot at my wireshark it dissects each single data packet as http</p></div><div id="comment-23196-info" class="comment-info"><span class="comment-age">(20 Jul '13, 06:29)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="23197"></span><div id="comment-23197" class="comment"><div id="post-23197-score" class="comment-score"></div><div class="comment-text"><p>Stream 30 in the re-arranged capture file does have a final chunk of 0 in frame 406, with all re-assembly options enabled at the TCP, SSL and HTTP layer, I get a normal "HTTP/1.1 200 OK" response in frame 406.</p></div><div id="comment-23197-info" class="comment-info"><span class="comment-age">(20 Jul '13, 07:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="23198"></span><div id="comment-23198" class="comment"><div id="post-23198-score" class="comment-score"></div><div class="comment-text"><p>Yes, the HTML part in frame 406 of the rearranged capture is what I wanted all along. I'm simply mystified how I wasted the whole day not seeing it.</p></div><div id="comment-23198-info" class="comment-info"><span class="comment-age">(20 Jul '13, 09:40)</span> <span class="comment-user userinfo">dansmith</span></div></div></div><div id="comment-tools-23195" class="comment-tools"></div><div class="clear"></div><div id="comment-23195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


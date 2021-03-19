+++
type = "question"
title = "Decoding Ethernet Encapsulated In TCP or UDP?"
description = '''Is there any way to get Wireshark to decode Ethernet frames that have been encapsulated/tunneled in a TCP (or UDP if that as easier) stream? I played around a bit with the &quot;Decode As...&quot; functionality but didn&#x27;t have any luck.'''
date = "2013-12-15T15:20:00Z"
lastmod = "2013-12-16T10:18:00Z"
weight = 28138
keywords = [ "tunnel", "decode", "decode_as" ]
aliases = [ "/questions/28138" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Decoding Ethernet Encapsulated In TCP or UDP?](/questions/28138/decoding-ethernet-encapsulated-in-tcp-or-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28138-score" class="post-score" title="current number of votes">0</div><span id="post-28138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to get Wireshark to decode Ethernet frames that have been encapsulated/tunneled in a TCP (or UDP if that as easier) stream? I played around a bit with the "Decode As..." functionality but didn't have any luck.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '13, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/f8ec1eb4cd05e70913046ca54d04ea6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Teddy%20P&#39;s gravatar image" /><p><span>Teddy P</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Teddy P has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '13, 15:22</strong> </span></p></div></div><div id="comments-container-28138" class="comments-container"><span id="28156"></span><div id="comment-28156" class="comment"><div id="post-28156-score" class="comment-score"></div><div class="comment-text"><p>what kind of encapsulation is this? Do you have a sample capture file you can post somewhere (google drive, dropbox, cloudshark.org, mega.co.nz)?</p></div><div id="comment-28156-info" class="comment-info"><span class="comment-age">(16 Dec '13, 06:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28166"></span><div id="comment-28166" class="comment"><div id="post-28166-score" class="comment-score"></div><div class="comment-text"><p>It is kind of an unusual situation. I'm fuzzing a common protocol using Peach Fuzzer. I'm developing on Windows, though I do most of my testing on Linux so I can send/receive raw Ethernet frames. Sometimes I need to switch back to Windows to debug Peach itself (but you can't use raw frames on Windows), so when I do that I encapsulate the raw frames in a TCP connection. It is nice to use Wireshark as a sanity check to make sure I'm generating the packets appropriately (or that they are getting fuzzed as expected), so having Wireshark look into that stream and decode it as if it were reading raw Ethernet is what I was trying to do.</p><p>Due to the lack of a useful loopback adapter in Windows, I appear to be stuck using RawCap to obtain these packets then opening the capture file from Wireshark to see them (and reopening that file as more packets come (<a href="http://ask.wireshark.org/questions/15674/wireshark-display-increasing-trace-file)).">http://ask.wireshark.org/questions/15674/wireshark-display-increasing-trace-file)).</a> Now that I've switched over to UDP per the suggestions below, I have a kludged together process that while not ideal (though considering the various factors I'm still pleased to be able to do it all) will suffice.</p></div><div id="comment-28166-info" class="comment-info"><span class="comment-age">(16 Dec '13, 09:29)</span> <span class="comment-user userinfo">Teddy P</span></div></div><span id="28167"></span><div id="comment-28167" class="comment"><div id="post-28167-score" class="comment-score"></div><div class="comment-text"><p>You could try running <code>Rawcap</code> from one command-line and Wireshark from another. Assuming you have cygwin's <code>tail</code> available, it would look something like so:</p><p>cmd1: <code>RawCap.exe -f 127.0.0.1 dumpfile.pcap</code></p><p>cmd2: <code>tail -c +0 -f dumpfile.pcap | Wireshark.exe -k -i -</code></p></div><div id="comment-28167-info" class="comment-info"><span class="comment-age">(16 Dec '13, 09:41)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="28168"></span><div id="comment-28168" class="comment"><div id="post-28168-score" class="comment-score"></div><div class="comment-text"><p>I had considered that based on the comments in the bug 5982 entry. I'll probably stick with hitting the 'Reload this capture file' button for now, but if I find myself doing this a lot I'll probably break down and install Cygwin. Good to have it as an option (and pointed out here with the question) though.</p></div><div id="comment-28168-info" class="comment-info"><span class="comment-age">(16 Dec '13, 10:18)</span> <span class="comment-user userinfo">Teddy P</span></div></div></div><div id="comment-tools-28138" class="comment-tools"></div><div class="clear"></div><div id="comment-28138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28140"></span>

<div id="answer-container-28140" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28140-score" class="post-score" title="current number of votes">3</div><span id="post-28140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Teddy P has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This can't currently be done with TCP packets, but it can be done with UDP packets by first selecting a relevant UDP packet and then right-clicking on the UDP layer in the packet details pane and choosing, <code>Decode As ...</code> followed by Ethernet and finally OK. You may need to change the port criteria, depending on your needs.</p><p>If you happen to have Ethernet encapsulated packets over TCP, then if you don't need the headers encapsulating the Ethernet frame, you should be able to use <a href="http://www.wireshark.org/docs/man-pages/editcap.html"><code>editcap</code></a> to chop off the bytes preceding the Ethernet header. Assuming there is a standard Ethernet, IP and TCP header preceding it, you would use something like the following:</p><pre><code>editcap -C 54 -F pcap infile.pcap outfile.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 17:36</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-28140" class="comments-container"></div><div id="comment-tools-28140" class="comment-tools"></div><div class="clear"></div><div id="comment-28140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28143"></span>

<div id="answer-container-28143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28143-score" class="post-score" title="current number of votes">1</div><span id="post-28143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there any way to get Wireshark to decode Ethernet frames that have been encapsulated/tunneled in a TCP (or UDP if that as easier) stream?</p></blockquote><p>For TCP, the encapsulation mechanism would have to include some mechanism for delimiting Ethernet frames, as there are <strong><em>NO</em></strong> packet boundaries visible to protocols running atop TCP; the protocol itself has to use some mechanism, such as a packet length field before each packet.</p><p>That would require that a dissector be written for the encapsulation protocol, as it wouldn't (because it <em>couldn't</em>) consist of raw Ethernet frames on a TCP connection.</p><p>For UDP, <em>IF</em> what's being encapsulated are raw Ethernet frames, you could use "Decode As..." to specify the port for the protocol, as per Chris Maynard's answer. If there's additional information preceding the raw Ethernet packet, you might have to have a dissector for the protocol; you might be able to write it in Lua if the version of Wireshark you're using has Lua support.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28143" class="comments-container"><span id="28163"></span><div id="comment-28163" class="comment"><div id="post-28163-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help Chris and Guy. Switching over to UDP and using "Decode As..." worked great.</p></div><div id="comment-28163-info" class="comment-info"><span class="comment-age">(16 Dec '13, 09:07)</span> <span class="comment-user userinfo">Teddy P</span></div></div></div><div id="comment-tools-28143" class="comment-tools"></div><div class="clear"></div><div id="comment-28143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Displaying all TCP connections with SYN packets"
description = '''Hello, I&#x27;m working on a rather large .pcap file, and I&#x27;m interested in displaying only the TCP connections that contain a SYN packet. Is there any way to do this?'''
date = "2010-09-20T10:44:00Z"
lastmod = "2011-06-07T16:02:00Z"
weight = 230
keywords = [ "connection", "syn", "tcp" ]
aliases = [ "/questions/230" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Displaying all TCP connections with SYN packets](/questions/230/displaying-all-tcp-connections-with-syn-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-230-score" class="post-score" title="current number of votes">0</div><span id="post-230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">3</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm working on a rather large .pcap file, and I'm interested in displaying only the TCP connections that contain a SYN packet. Is there any way to do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '10, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/832728debd1b180125e7979571c329f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmkastn&#39;s gravatar image" /><p><span>cmkastn</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmkastn has no accepted answers">0%</span></p></div></div><div id="comments-container-230" class="comments-container"></div><div id="comment-tools-230" class="comment-tools"></div><div class="clear"></div><div id="comment-230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="236"></span>

<div id="answer-container-236" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-236-score" class="post-score" title="current number of votes">2</div><span id="post-236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Loris Degioanni has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The display filter to show only SYN packets is:</p><pre><code>tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0</code></pre><p>If you only want to capture TCP/SYN packets, the capture filter would be:</p><pre><code>tcp[0xd]&amp;18=2</code></pre><p>When you are not only interested in the SYN packets, but also the SYN/ACK packets this changes to:</p><pre><code>tcp.flags.syn==1
tcp[0xd]&amp;2=2</code></pre><p>If I read your question in another way, you are looking for "all packets belonging to a TCP session for which the SYN packet is actually in the capture file". If this is your question, this can't be done directly with Wireshak. But you can do it by using <a href="http://wiki.wireshark.org/Mate">MATE</a> or <a href="http://wiki.wireshark.org/Lua">LUA</a>.</p><p>Or you can write a <a href="http://www.cacetech.com/sharkfest.10/A-6_Blok%20HANDS-ON%20LAB%20-%20Using%20Wireshark%20Command%20Line%20Tools%20and%20Scripting.zip">tshark script</a> to extract all the TCP sessions that have the initial SYN in the capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Sep '10, 10:56</strong> </span></p></div></div><div id="comments-container-236" class="comments-container"></div><div id="comment-tools-236" class="comment-tools"></div><div class="clear"></div><div id="comment-236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="232"></span>

<div id="answer-container-232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-232-score" class="post-score" title="current number of votes">1</div><span id="post-232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(tcp.flags.syn == 1 and tcp.flags.ack == 0) is the display filter you want</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/e458b44fd60b4064eb73fc42e67b3897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grossman&#39;s gravatar image" /><p><span>grossman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grossman has no accepted answers">0%</span></p></div></div><div id="comments-container-232" class="comments-container"><span id="233"></span><div id="comment-233" class="comment"><div id="post-233-score" class="comment-score"></div><div class="comment-text"><p>That will get you SYN packets only. Removing the "and tcp.flags.ack == 0" part will get you SYNs and SYN/ACKs.</p></div><div id="comment-233-info" class="comment-info"><span class="comment-age">(20 Sep '10, 10:49)</span> <span class="comment-user userinfo">grossman</span></div></div><span id="235"></span><div id="comment-235" class="comment"><div id="post-235-score" class="comment-score"></div><div class="comment-text"><p>That will show all packets that are SYN packets, but I want to see the complete connections for all connections that have SYN packets.</p></div><div id="comment-235-info" class="comment-info"><span class="comment-age">(20 Sep '10, 10:50)</span> <span class="comment-user userinfo">cmkastn</span></div></div><span id="237"></span><div id="comment-237" class="comment"><div id="post-237-score" class="comment-score"></div><div class="comment-text"><p>Ah. Hmm. Well, you could use the results of such a filter and then Right Click-&gt;Prepare A Filter-&gt;And Selected for the Stream Index under the TCP section of each SYN packet. Not exactly elegant, but that is the first thing that comes to mind.</p></div><div id="comment-237-info" class="comment-info"><span class="comment-age">(20 Sep '10, 10:55)</span> <span class="comment-user userinfo">grossman</span></div></div><span id="239"></span><div id="comment-239" class="comment"><div id="post-239-score" class="comment-score"></div><div class="comment-text"><p>Which can be automated with a little tshark scripting :-)</p></div><div id="comment-239-info" class="comment-info"><span class="comment-age">(20 Sep '10, 11:05)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-232" class="comment-tools"></div><div class="clear"></div><div id="comment-232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4442"></span>

<div id="answer-container-4442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4442-score" class="post-score" title="current number of votes">1</div><span id="post-4442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With the release of Wireshark 1.6.0, and thanks to some code changes by Sake Blok, you can now show all conversations that have their three-way handshake in the trace file with the display filter "tcp.window_size_scalefactor!=-1".</p><p>Note that this will show each CONVERSATION whose three-way handshake is present in the trace file, but it won't show the SYN packet or the SYN/ACK packet. The display will start with the third packet of the three-way handshake for each conversation. To see everything, select the stream you're interested in and then select "Follow TCP Stream."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4442" class="comments-container"><span id="4443"></span><div id="comment-4443" class="comment"><div id="post-4443-score" class="comment-score">2</div><div class="comment-text"><p>That was indeed a nice semi-planned by-product from my code change... Glad to see it got picked up :-)</p><p>Well, since we're looking for all conversations that do have the 3-way handshake in the tracefile, adding all the SYN packets will not harm us here. So you could use:</p><pre><code>tcp.flags.syn==1 or tcp.window_size_scalefactor!=-1</code></pre></div><div id="comment-4443-info" class="comment-info"><span class="comment-age">(07 Jun '11, 14:17)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4445"></span><div id="comment-4445" class="comment"><div id="post-4445-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Sake. That's what we're looking for. Question: In bug 5541, you said that the three values were going to be:</p><p>-1: 3WHS missing 0: No scaling negotiated, using the real value. 1 &amp; higher powers of two: scaling has been negotiated &amp; the window_size has been calculated accordingly</p><p>I see the following in the packet details pane:</p><p>[Window size scaling factor: -2 (no window scaling used)]</p><p>tcp.window_size_scalefactor==-2 shows me the streams that don't use window scaling; tcp.window_size_scalefactor==0 doesn't display anything. So I guess "0" got changed to "-2" in the final code revision?</p></div><div id="comment-4445-info" class="comment-info"><span class="comment-age">(07 Jun '11, 15:07)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="4446"></span><div id="comment-4446" class="comment"><div id="post-4446-score" class="comment-score"></div><div class="comment-text"><p>Yes, while implementing, I wanted to be able to make a distinction between window scaling factor 0 and no window scaling used. Both will result in the window size not being scaled up, but they are completely different situations. So the values are:</p><ul><li>-2 : Either the client or the server did not negotiate(!) window scaling, so no window scaling used</li><li>-1 : We have not seen the 3WHS and can therefor not tell whether or not to use window scaling</li><li>0+ : We do window scaling and this is the announced(!) window scaling factor for this flow</li></ul><p>Hope this makes it clear...</p></div><div id="comment-4446-info" class="comment-info"><span class="comment-age">(07 Jun '11, 15:43)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4447"></span><div id="comment-4447" class="comment"><div id="post-4447-score" class="comment-score"></div><div class="comment-text"><p>Yes, that makes it clear. And I agree with distinguishing between the two situations. That was the original problem with bug 5541: Using the same name/value for things that are different.</p></div><div id="comment-4447-info" class="comment-info"><span class="comment-age">(07 Jun '11, 16:02)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-4442" class="comment-tools"></div><div class="clear"></div><div id="comment-4442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="248"></span>

<div id="answer-container-248" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-248-score" class="post-score" title="current number of votes">0</div><span id="post-248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For anyone who's curious, this bash script seems to work. I'm sure there's an easier way to do it, but I'm not the best scripter in the world.</p><pre><code>#!/bin/bash

file=$1
outfile=$2

string=&quot;&quot;
counter=0

for src in `tshark -r $file -R &quot;tcp.flags.syn == 1&quot; -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport | cut -d &#39; &#39; -f1-4`
do
    if [ $counter == 0 ]; then
        string=$string&quot;(ip.src == $src &amp;&amp; &quot;
    elif [ $counter == 1 ]; then
        string=$string&quot;ip.dst == $src &amp;&amp; &quot;
    elif [ $counter == 2 ]; then
        string=$string&quot;tcp.srcport == $src &amp;&amp; &quot;
    else
        string=$string&quot;tcp.dstport == $src) || &quot; 
    fi

    if [ $counter == 3 ]; then
        let counter=0
    else
        let counter=$counter+1
    fi 
done

string=${string%????}

tshark -r $file -R &quot;$string&quot; -w &quot;$outfile&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/832728debd1b180125e7979571c329f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmkastn&#39;s gravatar image" /><p><span>cmkastn</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmkastn has no accepted answers">0%</span></p></div></div><div id="comments-container-248" class="comments-container"></div><div id="comment-tools-248" class="comment-tools"></div><div class="clear"></div><div id="comment-248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="309"></span>

<div id="answer-container-309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-309-score" class="post-score" title="current number of votes">0</div><span id="post-309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I only want to see the SYN-Flag (and not also SYN/ACK or funky flag combinations created by OS fingerprinting tools like nmap) I usually go for</p><p>"tcp.flags==0x02"</p><p>I used to do it like Sake suggested with the "tcp.flags.syn==1 and tcp.flags.ack==0", but I'm lazy and since my memory now allows me to remember the shorter version with "0x02" I use that :-)</p><p>Oh, and maybe this helps: if you want to avoid loading the whole trace and then filter it, you can also use the "tcp.flags==0x02" as a load filter in the open file dialog. That will then only load the frames that match and allow faster processing afterwards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '10, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '10, 02:55</strong> </span></p></div></div><div id="comments-container-309" class="comments-container"></div><div id="comment-tools-309" class="comment-tools"></div><div class="clear"></div><div id="comment-309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


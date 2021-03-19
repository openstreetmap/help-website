+++
type = "question"
title = "Plot time-series graph for number of TCP packets per 1 second. The X-axis should start with zero."
description = '''Anyone know how to do this, please help me. You can answer with any programming language such as Java, or programming R. Thank you in advance!!!'''
date = "2013-11-29T23:20:00Z"
lastmod = "2013-12-01T22:15:00Z"
weight = 27584
keywords = [ "r" ]
aliases = [ "/questions/27584" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plot time-series graph for number of TCP packets per 1 second. The X-axis should start with zero.](/questions/27584/plot-time-series-graph-for-number-of-tcp-packets-per-1-second-the-x-axis-should-start-with-zero)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27584-score" class="post-score" title="current number of votes">0</div><span id="post-27584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone know how to do this, please help me. You can answer with any programming language such as Java, or programming R. Thank you in advance!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '13, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/f6794f3ef18ab7a1ad2e4f56711db6f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eliza%20Rana&#39;s gravatar image" /><p><span>Eliza Rana</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eliza Rana has no accepted answers">0%</span></p></div></div><div id="comments-container-27584" class="comments-container"></div><div id="comment-tools-27584" class="comment-tools"></div><div class="clear"></div><div id="comment-27584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27592"></span>

<div id="answer-container-27592" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27592-score" class="post-score" title="current number of votes">2</div><span id="post-27592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>You can <strong>answer with any programming language</strong></p></blockquote><p>O.K. Then I choose Perl.</p><pre><code>#!/usr/bin/perl

use GUI::Testing;

$wireshark_bin = `which wireshark`;
chomp($wireshark_bin);

$capture_file  = &#39;input.pcap&#39;;

if ($pid = fork()) {
   # parent process ....

   # wait while Wireshark is starting ...
   sleep(30);

   # get a GUI handle for Wireshark
   $ws_handle = get_gui_handle($wireshark_bin);

   # get a handle for the IO Graph
   $io_graph = $ws_handle.menu(&quot;Statistics::IO Graph&quot;);

   $io_graph.tick_interval = &quot;1&quot;;
   $io_graph.pixel_per_tick = &quot;5&quot;;
   $io_graph.y_axis_unit = &quot;packets/tick&quot;;
   $io_graph.y_axis_scale = &quot;auto&quot;;

   # set the display filter for graph 1. 
   # Alternative filter: tcp.stream eq 2
   # Alternative filter: tcp.port eq 80
   $io_graph.graph_1.filter = &quot;tcp&quot;;

   $io_graph.graph_1.style = &quot;line&quot;;
   $io_graph.graph_1.redraw();

   $data = $io_graph.copy_data();

   analyze_data($data);

} else {
  # child process
  system(&quot;$wireshark_bin -nr $capture_file&quot;);
}

sub analyze_data {

   my $data = shift;

   print STDERR &quot;Please write your own code to analyze the data\n&quot;;
   print STDERR &quot;like calculation of mean or median values\n&quot;;
}</code></pre><p>Hint: 'Listen' to the code .....</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '13, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Nov '13, 15:48</strong> </span></p></div></div><div id="comments-container-27592" class="comments-container"><span id="27595"></span><div id="comment-27595" class="comment"><div id="post-27595-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for ur help, Kurt!!! I will install Perl and try this code...I would like to ask u one more question:</p><p>I want to transform the pcap file to csv file by using tshark command, but I got "Access is denied".</p><p>Here is what i wrote: tshark -r "d:\test.pcap" -T fields -e frame.time -e ip.proto -e frame.len -E header=y -E separator=, &gt; "d:\file.csv"</p></div><div id="comment-27595-info" class="comment-info"><span class="comment-age">(30 Nov '13, 21:02)</span> <span class="comment-user userinfo">Eliza Rana</span></div></div><span id="27596"></span><div id="comment-27596" class="comment"><div id="post-27596-score" class="comment-score"></div><div class="comment-text"><p>Note: I want to transform only the following datas into csv format: - Timestamp - Protocol - Packet_length <strong>Timestamp must be with a format that we can understand. for example, 20/01/2013 00:00:00</strong> And for protocol: I want to show only the top-level protocol such as TCP, UDP, etc.</p></div><div id="comment-27596-info" class="comment-info"><span class="comment-age">(30 Nov '13, 21:03)</span> <span class="comment-user userinfo">Eliza Rana</span></div></div><span id="27601"></span><div id="comment-27601" class="comment"><div id="post-27601-score" class="comment-score"></div><div class="comment-text"><blockquote><p>"Access is denied".</p></blockquote><p>hm... if <strong>my</strong> Windows shows that message, it usually want's to tell me that I am not allowed to read or write a file. Maybe <strong>your</strong> Windows is doing that too!?!</p></div><div id="comment-27601-info" class="comment-info"><span class="comment-age">(01 Dec '13, 03:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27603"></span><div id="comment-27603" class="comment"><div id="post-27603-score" class="comment-score"></div><div class="comment-text"><p>So what should i do kurt? Any other solution? Is what I wrote correct or not?</p></div><div id="comment-27603-info" class="comment-info"><span class="comment-age">(01 Dec '13, 05:00)</span> <span class="comment-user userinfo">Eliza Rana</span></div></div><span id="27604"></span><div id="comment-27604" class="comment not_top_scorer"><div id="post-27604-score" class="comment-score"></div><div class="comment-text"><p>If I want to use tshark command in windows, do i have to install Cygwin or just use the cmd command prompt? I really don't know about this.</p></div><div id="comment-27604-info" class="comment-info"><span class="comment-age">(01 Dec '13, 05:05)</span> <span class="comment-user userinfo">Eliza Rana</span></div></div><span id="27610"></span><div id="comment-27610" class="comment"><div id="post-27610-score" class="comment-score">2</div><div class="comment-text"><p>No need for Cygwin to run tshark, it will run from a cmd prompt (or a PowerShell one).</p></div><div id="comment-27610-info" class="comment-info"><span class="comment-age">(01 Dec '13, 08:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="27638"></span><div id="comment-27638" class="comment not_top_scorer"><div id="post-27638-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much grahamb...</p></div><div id="comment-27638-info" class="comment-info"><span class="comment-age">(01 Dec '13, 22:15)</span> <span class="comment-user userinfo">Eliza Rana</span></div></div></div><div id="comment-tools-27592" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-27592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


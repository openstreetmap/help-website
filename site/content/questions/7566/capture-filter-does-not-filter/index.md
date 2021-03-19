+++
type = "question"
title = "capture filter does not filter"
description = '''version 1.6.4, Windows 7, 64 bit, connected to a router then a cable modem. Start WireShark then select Capture -&amp;gt; Captures Filters ... Enter Filter name: &quot;aaa&quot; Filter String: &quot;src port 64.4.231.55&quot; then Select New and restart the capture. The captured packets include data other than those with a...'''
date = "2011-11-22T15:52:00Z"
lastmod = "2011-11-23T00:17:00Z"
weight = 7566
keywords = [ "filter", "capture" ]
aliases = [ "/questions/7566" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [capture filter does not filter](/questions/7566/capture-filter-does-not-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>version 1.6.4, Windows 7, 64 bit, connected to a router then a cable modem. Start WireShark then select Capture -&gt; Captures Filters ... Enter Filter name: "aaa" Filter String: "src port 64.4.231.55" then Select New and restart the capture. The captured packets include data other than those with a source other than specified. How do I get the capture to work? Thanks for your time</p></div><div id="question-tags" class="tags-container tags">filter capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '11, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/68c6ec7e9c6a5614e85d20345c5597e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkelly&#39;s gravatar image" /><p>bkelly<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkelly has no accepted answers">0%</span></p></div></div><div id="comments-container-7566" class="comments-container"></div><div id="comment-tools-7566" class="comment-tools"></div><div class="clear"></div><div id="comment-7566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7577"></span>

<div id="answer-container-7577" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7577-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you select "Capture -&gt; Capture Filters" you will get a window in which you can define, alter and delete capture filters for future use. You can't actually activate a capture filter from there.</p><p>One of the reasons is that some capture filters might work on some physical interfaces while they might not work on others. That's why you need to activate a capture filter with the capture options when you start your capture session.</p><p>Go to "Capture -&gt; Options" and use the "Capture Filter" button to select your pre-defined capture filter. Or just type the filter you need in the dialog box.</p><p>If you're using version 1.7.0 (or higher), you will need to doubleclick on the interface you are going to capture from first, as you can capture on multiple interfaces at once beginning with version 1.7.0 and you can set the capture filter differently for each interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '11, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7577" class="comments-container"><span id="7579"></span><div id="comment-7579" class="comment"><div id="post-7579-score" class="comment-score"></div><div class="comment-text"><p>That did the trick. That path I followed, in my not so humble opinion, shoud have worked. And when I follow this path and bring up options again, it does not show the filter currently in use. The user cannot build on what has already been entered. Making these two changes would be a significant improvement.</p><p>That said, Again I must say, thank you for the information and for taking time to post. This does help. You just started out my day on an excelent note.</p></div><div id="comment-7579-info" class="comment-info"><span class="comment-age">(23 Nov '11, 04:21)</span> bkelly</div></div><span id="7580"></span><div id="comment-7580" class="comment"><div id="post-7580-score" class="comment-score"></div><div class="comment-text"><p>I made significant progress as noted above. Now I am having trouble filtering out some packets. this works:<br />
</p><p>host 192.10.11.227</p><p>But these are rejected:</p><p>host 192.10.11.227 and not proto arp</p><p>host 192.10.11.227 and proto not arp</p><p>proto not arp and host 192.10.11.227</p><p>not proto arp and host 192.10.11.227</p><p>So I went to an extreme and entered only</p><p>proto arp</p><p>which was rejected. From my reading of the help file, some of these should be valid, and certainly the last should be. So here is my question:</p><p>What expression is required to get all packets to and from host 192.10.11.227 while rejecting all ARP packets?</p></div><div id="comment-7580-info" class="comment-info"><span class="comment-age">(23 Nov '11, 07:01)</span> bkelly</div></div><span id="7581"></span><div id="comment-7581" class="comment"><div id="post-7581-score" class="comment-score"></div><div class="comment-text"><p>ARP is not a protocol that runs on-top of IP, but at the same level as IP, therefor "(ip) proto arp" is not a valid expression.</p><p>What you want is:</p><pre><code>host 192.10.11.227 and not arp</code></pre><p>Regarding your path to a filter. I agree it would be nice to be able to make a capture filter active from the "Capture -&gt; Filters" dialog. However, there are two main problems with that path:</p><p>1) Not all capture filters are valid on all interfaces. For example "ether host 00:11:22:33:44:55" is not valid on a PPP interface.</p><p>2) You can't change a capture filter on a running job (yet)</p></div><div id="comment-7581-info" class="comment-info"><span class="comment-age">(23 Nov '11, 07:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-7577" class="comment-tools"></div><div class="clear"></div><div id="comment-7577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7568"></span>

<div id="answer-container-7568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7568-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Two comments:</p><ol><li>"src port 64.4.231.55" ??</li></ol><p>Do you mean "src host ..." ?</p><ol><li>Are you starting from the "Capture Options" window to set the Capture Filter ? Specifically: Do Capture ! Options then select the Capture Filters button.</li></ol><p>Just creating a named Capture Filter in the Capture Filters window directly doesn't actually set the capture filter to be used on an interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Nov '11, 17:53</p></div></div><div id="comments-container-7568" class="comments-container"></div><div id="comment-tools-7568" class="comment-tools"></div><div class="clear"></div><div id="comment-7568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7569"></span>

<div id="answer-container-7569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7569-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the "<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">Filtering while capturing</a>" section of the user guide, along with the information hyperlinked from that page, should provide all the help you need, not just for this particular filtering operation, but for any other capture filter you (and others) might need in the future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-7569" class="comments-container"><span id="7570"></span><div id="comment-7570" class="comment"><div id="post-7570-score" class="comment-score"></div><div class="comment-text"><p>I had the wrong phrase so I changed it to "src host 69.4.231.55", clicked OK, and none of the packets were from that host.</p><p>Re: 1.Are you starting from the "Capture Options" window to set the Capture Filter ? Specifically: Do Capture ! Options then select the Capture Filters button.</p><p>I am not sure I am reading you correctly. If I provide my steps maybe you can identify my error.</p><p>I start WireShark then select the one interface and click start. From the menu bar between Go and Analyze I select Capture then menu item Capture Filters. Having done this a few times I scroll the window down and select "aaa" That puts "aaa" in the filter name and "src host 69.4.231.55" in the Filter string: Then I click OK. Then I select the tool "Restart the running live capture." After that I do something like click a link in another tab (as I type this in.) There are all kinds of packets captured other than from the host specified.</p><p>EDIT: From the help file I read:<br />
</p><p>Example 4.1. A capture filter for telnet that captures traffic to and from a particular host</p><p>tcp port 23 and host 10.0.0.5</p><p>And presume that if I enter "host 69.4.231.55" I should see packets only from that one host. I tried exactly that and it did not filter.</p></div><div id="comment-7570-info" class="comment-info"><span class="comment-age">(22 Nov '11, 18:09)</span> bkelly</div></div><span id="7576"></span><div id="comment-7576" class="comment"><div id="post-7576-score" class="comment-score"></div><div class="comment-text"><p>(Oops, I converted your answer to a comment on the answer to which it doesn't belong. However, please use "add comment" to respond to answers. Have a look at the FAQ for more details)</p></div><div id="comment-7576-info" class="comment-info"><span class="comment-age">(23 Nov '11, 00:10)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-7569" class="comment-tools"></div><div class="clear"></div><div id="comment-7569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


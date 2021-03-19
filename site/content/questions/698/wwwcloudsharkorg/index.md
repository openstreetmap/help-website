+++
type = "question"
title = "www.Cloudshark.org"
description = '''I just stumbled onto this site tonight. You can look at .pcap files in a web browser. I thought it was pretty cool in a pinch.'''
date = "2010-10-26T23:54:00Z"
lastmod = "2010-10-28T09:03:00Z"
weight = 698
keywords = [ "cloudshark" ]
aliases = [ "/questions/698" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [www.Cloudshark.org](/questions/698/wwwcloudsharkorg)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-698-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just stumbled onto this site tonight. You can look at .pcap files in a web browser. I thought it was pretty cool in a pinch.</p></div><div id="question-tags" class="tags-container tags">cloudshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '10, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/e12b8d5f904f018189f5cf3c69cbe5f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Owen&#39;s gravatar image" /><p>Owen<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Owen has no accepted answers">0%</span></p></div></div><div id="comments-container-698" class="comments-container"><span id="712"></span><div id="comment-712" class="comment"><div id="post-712-score" class="comment-score"></div><div class="comment-text"><p>Unable to load Capture: The file is too large to import. Please limit files to 512,000 bytes</p></div><div id="comment-712-info" class="comment-info"><span class="comment-age">(27 Oct '10, 14:07)</span> net_tech</div></div><span id="785"></span><div id="comment-785" class="comment"><div id="post-785-score" class="comment-score"></div><div class="comment-text"><p>Just to address the 512K limitation ... We recently rolled out a CloudShark update that increases the uploaded capture file size to 5 Megabytes.</p><p><a href="http://beach.cloudshark.org/post/1464674390/cloudshark-november-updates">http://beach.cloudshark.org/post/1464674390/cloudshark-november-updates</a></p><p>The update includes navigation sparklines and infinite scrolling.</p></div><div id="comment-785-info" class="comment-info"><span class="comment-age">(02 Nov '10, 16:37)</span> cloudshark</div></div><span id="1351"></span><div id="comment-1351" class="comment"><div id="post-1351-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link, it is a very interesting resource. I work with Cisco and I find it to be one more useful tool in my toolbox.</p><p>If somebody ever comes up with a way to embed packet captures on a web page similar to what I posted in my initial question, would be much appreciated.</p></div><div id="comment-1351-info" class="comment-info"><span class="comment-age">(14 Dec '10, 18:35)</span> jpms</div></div></div><div id="comment-tools-698" class="comment-tools"></div><div class="clear"></div><div id="comment-698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="704"></span>

<div id="answer-container-704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-704-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the opportunity to shed some light on why we created <a href="http://www.cloudshark.org">CloudShark.org</a>. We original developed the browser based decode idea to work with our own product CDRouter developed by <a href="http://www.qacafe.com">QA Cafe</a>.</p><p>Once we saw this working with CDRouter, it made sense to break this out into a stand alone site and CloudShark.org was born.</p><p>I am not going to debate the security concerns of sending a capture file into the cloud. This does not make sense in many cases. The security issue is true of many cloud applications. But there are a number of situations where having a browser based solution is extremely helpful.</p><p>Consider the following ...</p><p>1) Web sites that host example capture files can now integrate those capture files into the browsing experience. This makes the capture file more accessible to anyone browsing the site. This is great for education and training sites. Take a look at what PacketLife has done with their capture examples. <a href="http://packetlife.net/captures/">http://packetlife.net/captures/</a></p><p>2) Wireshark is not always available on every computing platform. For example, iPads, smart phones, etc. Even if Wireshark does support the OS, it may not be installed and you may not be allowed to install it. Consider a public terminal. In these situations, CloudShark is very helpful.</p><p>3) A CloudShark URL can point to a specific packet in a capture file and make linking very easy. This makes it easy to share a packet with a non-wireshark user.</p><p>Most of the feedback we have received on CloudShark has been positive. Many security minded folks have pointed out the risk of sending capture files into the cloud.</p><p>Certainly, CloudShark is not a complete replacement for running Wireshark locally. But the cloud concept does have merit to many situations where you need to look at a capture file. It is up to the user to decide when this is appropriate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/3296169772fdefbaaa84fed7f8fe6591?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cloudshark&#39;s gravatar image" /><p>cloudshark<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cloudshark has no accepted answers">0%</span></p></div></div><div id="comments-container-704" class="comments-container"><span id="710"></span><div id="comment-710" class="comment"><div id="post-710-score" class="comment-score"></div><div class="comment-text"><p>Thanks for giving us some insight into CloudShark.org. Appreciate your participation.</p></div><div id="comment-710-info" class="comment-info"><span class="comment-age">(27 Oct '10, 12:15)</span> lchappell ♦</div></div><span id="7247"></span><div id="comment-7247" class="comment"><div id="post-7247-score" class="comment-score"></div><div class="comment-text"><p>A couple updates to this thread ...</p><ul><li><p>Since this thread was started, we introduced the CloudShark appliance to let folks run CloudShark in their own networks. This addressed the security concerns of uploading capture files to the cloud. The appliance can run in a vm or directly on hardware.</p></li><li><p>We just added several new analysis features to cloudshark.org and bumped the upload size to 10M for the free version.</p></li></ul></div><div id="comment-7247-info" class="comment-info"><span class="comment-age">(05 Nov '11, 09:44)</span> joemc</div></div></div><div id="comment-tools-704" class="comment-tools"></div><div class="clear"></div><div id="comment-704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="699"></span>

<div id="answer-container-699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-699-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>&lt;opinion&gt; Let's see... upload a trace file containing my company's communications to a "cloud" server... do my analysis there as opposed to doing it on my own system in the safety of my network... Uh... what exactly did I gain?</p><p>A good friend sent me this quote and the source is unknown... perhaps someone can find it for me... <strong>"The Cloud is like sex in high school. Everyone is talking about it, few people doing it. None are good at it."</strong></p><p>I hate to "rain" on the cloud parade, but... reading the FAQ...</p><p><em>"While the URLs to your decode session are not publicly shared, we make no claims that your data is not viewable by other CloudShark users. For now, if you want to protect sensitive data in your capture files, don't use CloudShark."</em></p><p>No jabs at Cloudshark at all... they found an opportunity and it's an interesting one.</p><p>What happens when you can't upload that corporate trace file someday to that site... take a trace of your upload to the cloud and... wait for the "cloud" to support that upload someday?</p><p>After an interesting invitation to speak on cloud computing at TechEd 2010, I reveled in the opportunity to sit on a tech-savvy panel and address the issue of "you hate your ISP now, but you'll rely on them for your full corporate communication system...?" I defer to the brilliant likes of Guy Harris to speak to the Wireshark community on the advantages/disadvantages of using/analyzing in the cloud community... Guy?</p><p>My quick thoughts here as I wrap up a long day of recording - could someone explain why it would be advantageous to upload a trace file to the "cloud" to analyze it rather than just run Wireshark and look at the packets? &lt;opinion off&gt;</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '10, 00:47</p></div></div><div id="comments-container-699" class="comments-container"></div><div id="comment-tools-699" class="comment-tools"></div><div class="clear"></div><div id="comment-699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="724"></span>

<div id="answer-container-724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-724-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As pcap file gets uploaded to the site, there is no status or progress bar for the upload. So you have to run wireshark on your computer locally anyway to see if data is being sent :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-724" class="comments-container"></div><div id="comment-tools-724" class="comment-tools"></div><div class="clear"></div><div id="comment-724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="729"></span>

<div id="answer-container-729" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-729-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm 100% in agreement with Laura. Why would I want to upload corporate information to the cloud, period? On a daily basis I defend my resolve not to depend on the cloud for certain types of information.</p><p>I took notes at that TechEd2010 panel discussion. There were some great points made about the inability to analyze your own information once control has been passed to a cloud provider. As an information security and business continuity specialist, the last thing I want is to lose control of my organization's information. Not only do I want to know our information is tucked in safe and sound, but who is accessing it how and when. And I want to be able to prove that with proper analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/6723c4a3c1d95d32245dd8dc9a05712a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roberta%20Osmers&#39;s gravatar image" /><p>Roberta Osmers<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roberta Osmers has no accepted answers">0%</span></p></div></div><div id="comments-container-729" class="comments-container"></div><div id="comment-tools-729" class="comment-tools"></div><div class="clear"></div><div id="comment-729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


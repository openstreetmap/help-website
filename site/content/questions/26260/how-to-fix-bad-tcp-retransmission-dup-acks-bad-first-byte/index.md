+++
type = "question"
title = "How to fix Bad TCP - Retransmission &amp; Dup ACKs - Bad First Byte."
description = '''My website has seen ever decreasing traffic, so I&#x27;ve been working to increase speed and usability. On WebPageTest.org I&#x27;ve worked most of my grades up but First Byte is still horrible.  F First Byte Time A Keep-alive Enabled A Compress Transfer A Compress Images A Progressive JPEGs B Cache static   ...'''
date = "2013-10-21T14:39:00Z"
lastmod = "2013-10-21T17:32:00Z"
weight = 26260
keywords = [ "dup-ack", "bad-tcp" ]
aliases = [ "/questions/26260" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix Bad TCP - Retransmission & Dup ACKs - Bad First Byte.](/questions/26260/how-to-fix-bad-tcp-retransmission-dup-acks-bad-first-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26260-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My website has seen ever decreasing traffic, so I've been working to increase speed and usability. On WebPageTest.org I've worked most of my grades up but First Byte is still horrible.</p><ul><li>F First Byte Time</li><li>A Keep-alive Enabled</li><li>A Compress Transfer</li><li>A Compress Images</li><li>A Progressive JPEGs</li><li>B Cache static</li></ul><p>First Byte Time (back-end processing): 0/100</p><p>1081 ms First Byte Time 90 ms Target First Byte Time</p><p>I did a packet capture (SeverSide) and analyzed it using wireshark. during a hit and leave visit to the site I got:</p><p>6 lines of BAD TCP happening at about lines 28-33 warning that I have TCP Retransmission and TCP Dup ACK... 2 of each of these warnings 3 times.</p><p>Under the expanded panel viewing a Retransmission/ TCP analysis flags - "retransmission suspected" "security level NOTE" RTO of 1.19 seconds.</p><p>Under the expanded panel viewing DCP Dup ACK/ TCP analysis flags - Duplicate ACK" "security level NOTE" RTT of 0.09 seconds.</p><p>I don't know if this is wise to do or not, but I've uploaded my packet capture dump file.</p><p><a href="http://www.aboveallhouseplans.com/tcpinfo.zip">http://www.aboveallhouseplans.com/tcpinfo.zip</a></p><p>example captures of flagged tcp.</p><pre><code>34  1.678330    198.61.171.121  173.30.226.94   TCP 66  [TCP Retransmission] http &gt; 62271 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1460 SACK_PERM=1 WS=128

37  1.733971    173.30.226.94   198.61.171.121  TCP 66  [TCP Dup ACK 28#1] 62267 &gt; http [ACK] Seq=1 Ack=1 Win=65700 Len=0 SLE=0 SRE=1</code></pre></div><div id="question-tags" class="tags-container tags">dup-ack bad-tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/1662e8d0f56c2c435fd080e4f4d76056?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krisidious&#39;s gravatar image" /><p>Krisidious<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krisidious has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '13, 15:20</p></div></div><div id="comments-container-26260" class="comments-container"></div><div id="comment-tools-26260" class="comment-tools"></div><div class="clear"></div><div id="comment-26260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26265"></span>

<div id="answer-container-26265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26265-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've accessed your page several times and I don't get any TCP retransmissions. The rating on WebPageTest.org is also pretty good, only the <code>First Byte Time</code> isn't rated very well. However, that rating depends on the test location. Furthermore the personal experience while loading the page does not reflect that bad rating, meaning the page loads in an acceptable time.</p><blockquote><p><strong>My website has seen ever decreasing traffic</strong>, so I've been working to increase speed and usability.</p></blockquote><p>I don't think this is related to network problems and/or the technical structure of the page, as there is no real problem.</p><p>The overall rating of <a href="http://www.microsoft.com">http://www.microsoft.com</a> is much worse than your page (in several categories) and I guess they don't have any problem with decreasing traffic.</p><p>So, there must be another reason and I see the following possible reasons for a decreasing number of visitors.</p><ul><li>people don't find your page. Compare <a href="http://www.alexa.com/siteinfo/aboveallhouseplans.com">your ranking on Alexa</a> with the <a href="http://www.alexa.com/siteinfo/houseplans.com">ranking of houseplans.com</a> (<strong>invest in SEO</strong>)</li><li>the content is no longer interesting for your former users (fix that somehow)</li><li>there are other pages with better and/or cheaper content similar to yours (do whatever is necessary). <code>Similar sites: http://www.topsimilarsites.com/similar-to/aboveallhouseplans.com</code></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '13, 17:35</p></div></div><div id="comments-container-26265" class="comments-container"><span id="26269"></span><div id="comment-26269" class="comment"><div id="post-26269-score" class="comment-score"></div><div class="comment-text"><p>The site is very responsive; just doesn't show well in those first few ms. I've read Google really likes a good FirstByte. Both Google Page Insights, WebPageTest and WebsiteOptimization show bad initial communication. I'm looking to fix this more from a ranking point of view than a networking one.</p><p>I don't think that normal SEO has much to do with it... I've been running this site for 12 years and I had slowly built up the traffic over that time. My traffic dropped drastically on or about April 24th of 2012 coinciding with the Google Penguin release. I was getting around 1000-1700 unique visitors per day. Then dropped to 300-500 and stayed. 1-2 months after this drop I took the opportunity to rebuild the entire site in a new system, A dynamic php based system instead of the static html I had used before.</p><p>Until recently I had an extensive and keyword rich category dropdown menu pushing keyword density really high. I hadn't noticed and so I killed the whole menu, then in order to gain more speed I moved the entire site over to this dedicated server and I've been tuning all the backend stuff. This is my last hump for scoring well.</p><p>Like Microsoft, HousePlans.com doesn't really have to try like I do, They're a conglomerate of other plan sites, they bought the big domain that was pretty old and they have thousands of links to them from affiliate programs and they pay an incredible amount of money in Adwords. They pay for many other avenues of advertising and as Google says, "if your site gets traffic, we'll send you more traffic". Many of the keywords I've gone after they have neglected until the see me in that spot, then they just take it. I used to be #1 for both Unique and Unusual House Plans, but now you can see who has it, even though their plans are neither unique or unusual.</p><p>If you run the many different reports, I beat them in many areas or I'm close to their score. They have a significant amount of links from both standard sites and social media, but I'm in line with other major sites for my product. Something else has to explain the dramatic drop. I've done my best never to engage in Black Hat type things, but sometimes you're doing something and then they decide it's black hat. Like link trading... I was a member of Linkmanager.com and I felt like it might have been the issue. Although I only added a few sites to my site each week and only relevant ones at that.</p><p>Anyway, I appreciate your advice and your taking the time to look at my issue.</p></div><div id="comment-26269-info" class="comment-info"><span class="comment-age">(21 Oct '13, 18:26)</span> Krisidious</div></div><span id="26278"></span><div id="comment-26278" class="comment"><div id="post-26278-score" class="comment-score"></div><div class="comment-text"><p>As I said, I don't think there is a technical problem with your site.</p></div><div id="comment-26278-info" class="comment-info"><span class="comment-age">(22 Oct '13, 00:28)</span> Kurt Knochner ♦</div></div><span id="26286"></span><div id="comment-26286" class="comment"><div id="post-26286-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Until recently I had an extensive and keyword rich category dropdown menu <strong>pushing keyword density really high</strong>.</p></blockquote><p>Isn't that exactly what's causing a bad rating with <a href="http://en.wikipedia.org/wiki/Google_Penguin">google Penguin</a>?</p><blockquote><p><a href="http://www.webdesignerdepot.com/2013/05/seo-sanity-check-part-1-googles-penguin-and-panda-updates/">http://www.webdesignerdepot.com/2013/05/seo-sanity-check-part-1-googles-penguin-and-panda-updates/</a></p></blockquote><p>Again, I don't think there is a technical problem with your site, at least nothing related to networking and thus nothing that the Wireshark community can help with.</p><p>I recommend the blog of Matt Cutts (head of Google’s Webspam team).</p><blockquote><p><a href="http://www.mattcutts.com/blog/">http://www.mattcutts.com/blog/</a></p></blockquote><p>Occasionally he seems to answers questions about changes of google ratings for certain web sites. Maybe you just ask him if there are any signs why (or if) your site received a 'penalty' from the google rating system.</p></div><div id="comment-26286-info" class="comment-info"><span class="comment-age">(22 Oct '13, 07:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26265" class="comment-tools"></div><div class="clear"></div><div id="comment-26265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


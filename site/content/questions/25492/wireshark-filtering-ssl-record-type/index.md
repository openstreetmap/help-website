+++
type = "question"
title = "Wireshark Filtering SSL record type"
description = '''Hello, i&#x27;m trying to filter some ssl record using ssl.record.content_type==22 but i&#x27;m facing a problem if a frame contains 22 and 23 for example, it appears is there a way i can force wireshark to filter the frames that &quot;ONLY&quot; contains 22 not 22 and 23 and w.e ? thanks for the help :)'''
date = "2013-10-02T00:25:00Z"
lastmod = "2013-10-02T11:17:00Z"
weight = 25492
keywords = [ "filter", "ssl" ]
aliases = [ "/questions/25492" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Filtering SSL record type](/questions/25492/wireshark-filtering-ssl-record-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25492-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i'm trying to filter some ssl record using ssl.record.content_type==22 but i'm facing a problem if a frame contains 22 and 23 for example, it appears is there a way i can force wireshark to filter the frames that "ONLY" contains 22 not 22 and 23 and w.e ? thanks for the help :)</p></div><div id="question-tags" class="tags-container tags">filter ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/27e19b1f6c0b00e4469bfa2fba760e79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziad%20Kiwan&#39;s gravatar image" /><p>Ziad Kiwan<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziad Kiwan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 02:04</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25492" class="comments-container"></div><div id="comment-tools-25492" class="comment-tools"></div><div class="clear"></div><div id="comment-25492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25542"></span>

<div id="answer-container-25542" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25542-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is one of the few cases where the "!=" operator does come in handy, the following filter should work too:</p><pre><code>ssl.record.content_type == 22 and not ssl.record.content_type != 22</code></pre><p>Which translates to:</p><p><em>There is an occurrence of field ssl.record.content_type that has the value 22 and there is not an occurrence of field ssl.record.content_type that does not have the value 22.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25542" class="comments-container"><span id="25556"></span><div id="comment-25556" class="comment"><div id="post-25556-score" class="comment-score"></div><div class="comment-text"><p>actually your filter works better than mine, as your filter only prints the frames with content_type 22, whereas my filter also prints frames with no content_type at all.</p><p>What's missing in my filter statement is: ssl.record.content_type == 22</p><p>The second part of your filter statement (not ssl.record.content_type != 22) is logically the same statement as the statement in my answer, only shorter.</p><p>Therefore your answer should be selected as the right one. I would have done it myself, but the system did not allow me to do it.</p><pre><code>according to De Morgan&#39;s law 1: (not a) and (not b) == not (a or b), the following

not ssl.record.content_type &gt; 22 and not ssl.record.content_type &lt; 22

is the same as 

not (ssl.record.content_type &gt; 22 or ssl.record.content_type &lt; 22)

whereas 

ssl.record.content_type &gt; 22 or ssl.record.content_type &lt; 22

is the same as 

ssl.record.content_type != 22

So

not ssl.record.content_type != 22

is the same as 

not ssl.record.content_type &gt; 22 and not ssl.record.content_type &lt; 22</code></pre></div><div id="comment-25556-info" class="comment-info"><span class="comment-age">(02 Oct '13, 14:22)</span> Kurt Knochner ♦</div></div><span id="25558"></span><div id="comment-25558" class="comment"><div id="post-25558-score" class="comment-score"></div><div class="comment-text"><p>Yes indeed the second part of my filter is logically the same as your filter. I was just happy to (finally) have an example where the "!=" operator is of use.</p><p>In my wireshark trainings I have always mentioned that there is a use case, but that I can't think of one... now I can :-)</p></div><div id="comment-25558-info" class="comment-info"><span class="comment-age">(02 Oct '13, 14:46)</span> SYN-bit ♦♦</div></div><span id="25559"></span><div id="comment-25559" class="comment"><div id="post-25559-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but that I can't think of one... now I can :-)</p></blockquote><p>Yep, although it's hard to understand if you look at it the first time, as it looks somehow 'not right', probably due to the double negation, which human brains can't handle well.</p><p>Anyway, this is something new I learned about Wireshark :-)</p><p>Please mark your answer as the correct one.</p></div><div id="comment-25559-info" class="comment-info"><span class="comment-age">(02 Oct '13, 14:53)</span> Kurt Knochner ♦</div></div><span id="25560"></span><div id="comment-25560" class="comment"><div id="post-25560-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Please mark your answer as the correct one.</p></blockquote><p>As you have moderator rights now, you should be able to do that yourself. Can you check?</p></div><div id="comment-25560-info" class="comment-info"><span class="comment-age">(02 Oct '13, 15:16)</span> SYN-bit ♦♦</div></div><span id="25561"></span><div id="comment-25561" class="comment"><div id="post-25561-score" class="comment-score"></div><div class="comment-text"><p>I did. It does not work.</p></div><div id="comment-25561-info" class="comment-info"><span class="comment-age">(02 Oct '13, 15:17)</span> Kurt Knochner ♦</div></div><span id="25578"></span><div id="comment-25578" class="comment not_top_scorer"><div id="post-25578-score" class="comment-score"></div><div class="comment-text"><p>I unchecked the first answer, then I could check the 2nd one.</p></div><div id="comment-25578-info" class="comment-info"><span class="comment-age">(03 Oct '13, 00:01)</span> grahamb ♦</div></div><span id="25582"></span><div id="comment-25582" class="comment not_top_scorer"><div id="post-25582-score" class="comment-score"></div><div class="comment-text"><p>Ah, very good. Thanks.</p></div><div id="comment-25582-info" class="comment-info"><span class="comment-age">(03 Oct '13, 02:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25542" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-25542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25494"></span>

<div id="answer-container-25494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25494-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><del>I did not test it, but this might work</del></p><del></del><blockquote><p><del></del></p><p><del>ssl.record.content_type==22 and not ssl.record.content_type==23</del></p></blockquote><p><strong>++ UPDATE ++</strong></p><p>Please try this (works on my system)</p><blockquote><p>not ssl.record.content_type &gt; 22 and not ssl.record.content_type &lt; 22</p></blockquote><p><strong>Sample #1:</strong></p><p>With the simple filter, you'll get frames with multiple (different) content types as well.</p><blockquote><p>tshark -nr ssl.pcap -T fields -R "ssl.record.content_type == 22" -e frame.number -e ssl.record.content_type</p></blockquote><p>Result:</p><pre><code>11      22
17      22
19      22,20,22
24      20,22
29      20,22
121     22</code></pre><p><strong>Sample #2:</strong></p><p>With the modified filter, you'll get only frames with exactly the content type 22.</p><blockquote><p>tshark -nr ssl.pcap -T fields -R "not ssl.record.content_type &gt; 22 and not ssl.record.content_type &lt; 22" -e frame.number -e ssl.record.content_type</p></blockquote><p>Result:</p><pre><code>10
11      22
12
13
14
15
16
17      22
18
20
...
229     22
230
231
232
235     22,22
236</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 08:02</p></div></div><div id="comments-container-25494" class="comments-container"><span id="25495"></span><div id="comment-25495" class="comment"><div id="post-25495-score" class="comment-score"></div><div class="comment-text"><p>there is a lot of ssl.record.content_type not only 23 there is too much</p></div><div id="comment-25495-info" class="comment-info"><span class="comment-age">(02 Oct '13, 00:52)</span> Ziad Kiwan</div></div><span id="25509"></span><div id="comment-25509" class="comment"><div id="post-25509-score" class="comment-score"></div><div class="comment-text"><p>O.K. maybe I misinterpreted your question. I thought you might have several SSL frames stacked in another protocol. Based on your last comment, that's probably not the case.</p><p>So, can you please rephrase your question? Because, if you use the following filter</p><blockquote><p>ssl.record.content_type==22</p></blockquote><p>you will only see frames with that content type (Handshake). The same holds true for 23.</p><blockquote><p>but i'm facing a problem if a frame contains 22 and 23 for example,</p></blockquote><p>How does that happen? Can you post a sample capture somewhere (google docs, dropbox, cloudshark).</p></div><div id="comment-25509-info" class="comment-info"><span class="comment-age">(02 Oct '13, 06:21)</span> Kurt Knochner ♦</div></div><span id="25512"></span><div id="comment-25512" class="comment"><div id="post-25512-score" class="comment-score"></div><div class="comment-text"><p>no sorry i don't have a sample on hands now,what is happening that when i use ssl.record.content_type==22 as a filter frame that contains content type 22 is appearing even the ones that contains 22 and 23 or even any other content type id and i want only the frames that contains ssl content type 22 exactly appear</p></div><div id="comment-25512-info" class="comment-info"><span class="comment-age">(02 Oct '13, 07:38)</span> Ziad Kiwan</div></div><span id="25513"></span><div id="comment-25513" class="comment"><div id="post-25513-score" class="comment-score"></div><div class="comment-text"><p>O.K. then we need a sample capture where that happens, because if I filter for content type 22 I only get those frames.</p><p>BTW: What is your OS and Wireshark version?</p></div><div id="comment-25513-info" class="comment-info"><span class="comment-age">(02 Oct '13, 07:41)</span> Kurt Knochner ♦</div></div><span id="25514"></span><div id="comment-25514" class="comment"><div id="post-25514-score" class="comment-score"></div><div class="comment-text"><p>Ubuntu 13.04 and wireshark 1.8.2</p></div><div id="comment-25514-info" class="comment-info"><span class="comment-age">(02 Oct '13, 07:43)</span> Ziad Kiwan</div></div><span id="25516"></span><div id="comment-25516" class="comment not_top_scorer"><div id="post-25516-score" class="comment-score"></div><div class="comment-text"><p>O.K. nothing suspicious with those.</p><p>So again, we need a sample capture file where it happens what you describe.</p></div><div id="comment-25516-info" class="comment-info"><span class="comment-age">(02 Oct '13, 07:45)</span> Kurt Knochner ♦</div></div><span id="25518"></span><div id="comment-25518" class="comment not_top_scorer"><div id="post-25518-score" class="comment-score"></div><div class="comment-text"><p>O.K. now I got what you wanted. Please see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-25518-info" class="comment-info"><span class="comment-age">(02 Oct '13, 07:55)</span> Kurt Knochner ♦</div></div><span id="25522"></span><div id="comment-25522" class="comment not_top_scorer"><div id="post-25522-score" class="comment-score"></div><div class="comment-text"><p>i think that its thanks for the help! real appreciated!</p></div><div id="comment-25522-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:13)</span> Ziad Kiwan</div></div><span id="25523"></span><div id="comment-25523" class="comment not_top_scorer"><div id="post-25523-score" class="comment-score"></div><div class="comment-text"><p>Hello i tried it now it didn't work :/ 22 isn't appearing at all now idk why</p></div><div id="comment-25523-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:16)</span> Ziad Kiwan</div></div><span id="25525"></span><div id="comment-25525" class="comment not_top_scorer"><div id="post-25525-score" class="comment-score"></div><div class="comment-text"><p>well, it works on my system, however I used Wireshark 1.10.2.</p></div><div id="comment-25525-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:19)</span> Kurt Knochner ♦</div></div><span id="25526"></span><div id="comment-25526" class="comment not_top_scorer"><div id="post-25526-score" class="comment-score"></div><div class="comment-text"><p>I did a quick test with 1.8.6 (Windows XP) and it works as well.</p></div><div id="comment-25526-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:21)</span> Kurt Knochner ♦</div></div><span id="25527"></span><div id="comment-25527" class="comment not_top_scorer"><div id="post-25527-score" class="comment-score"></div><div class="comment-text"><p>never mind something is messing with my filter now i need to find it out thanks for the help tho</p></div><div id="comment-25527-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:23)</span> Ziad Kiwan</div></div><span id="25528"></span><div id="comment-25528" class="comment not_top_scorer"><div id="post-25528-score" class="comment-score"></div><div class="comment-text"><p>here is a sample file:</p><blockquote><p><a href="http://cloudshark.org/captures/8ba3ffa30008">http://cloudshark.org/captures/8ba3ffa30008</a></p></blockquote><p>Please run these two commands and post the output (only part of it) here.</p><blockquote><p>tshark -nr ssl_filtered.pcap -T fields -R "not ssl.record.content_type &gt; 22 and not ssl.record.content_type &lt; 22" -e frame.number -e ssl.record.content_type</p><p>tshark -nr ssl_filtered.pcap -T fields -R "ssl.record.content_type == 22" -e frame.number -e ssl.record.content_type</p></blockquote></div><div id="comment-25528-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:27)</span> Kurt Knochner ♦</div></div><span id="25529"></span><div id="comment-25529" class="comment not_top_scorer"><div id="post-25529-score" class="comment-score"></div><div class="comment-text"><p>its fine i found the problem now when i forgot replaced the old filter with the new one i messed up it messed up a bit thanks again</p></div><div id="comment-25529-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:29)</span> Ziad Kiwan</div></div></div><div id="comment-tools-25494" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-25494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Search In:Packet list not working on a particular interface."
description = '''In wireshark 1.8.5, for wimax-btsCapc interface, searching for a packet through Packet list doesn&#x27;t show any output. But searching for the same through &#x27;Packet Details&#x27; option works. Where could be the probable defect?'''
date = "2013-09-25T01:08:00Z"
lastmod = "2013-10-01T03:32:00Z"
weight = 25188
keywords = [ "search" ]
aliases = [ "/questions/25188" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Search In:Packet list not working on a particular interface.](/questions/25188/search-inpacket-list-not-working-on-a-particular-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25188-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark 1.8.5, for wimax-btsCapc interface, searching for a packet through Packet list doesn't show any output. But searching for the same through 'Packet Details' option works. Where could be the probable defect?</p></div><div id="question-tags" class="tags-container tags">search</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/dd64de546bcf7652a4faed163ff02df0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunshine&#39;s gravatar image" /><p>sunshine<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunshine has no accepted answers">0%</span></p></div></div><div id="comments-container-25188" class="comments-container"></div><div id="comment-tools-25188" class="comment-tools"></div><div class="clear"></div><div id="comment-25188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25429"></span>

<div id="answer-container-25429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not all packet details are available in the packet list (there is only a summary line), so a "string" search will not find the same packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25429" class="comments-container"><span id="25453"></span><div id="comment-25453" class="comment"><div id="post-25453-score" class="comment-score"></div><div class="comment-text"><p>What can be done to include all the packets for string search through List?</p></div><div id="comment-25453-info" class="comment-info"><span class="comment-age">(01 Oct '13, 03:15)</span> sunshine</div></div><span id="25456"></span><div id="comment-25456" class="comment"><div id="post-25456-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand your question. Do you want to display all packets that contain a certain string? You could use the display filter "frame contains &lt;string&gt;" for that.</p></div><div id="comment-25456-info" class="comment-info"><span class="comment-age">(01 Oct '13, 03:31)</span> SYN-bit ♦♦</div></div><span id="25461"></span><div id="comment-25461" class="comment"><div id="post-25461-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Issue is with the custom-dissector</p></blockquote><p>If you have written your dissector to generate (named) fields, then you can filter on those fields.</p><p>What is the data you want to filter on and how did you add the data to the "tree" in your dissector?</p></div><div id="comment-25461-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:19)</span> SYN-bit ♦♦</div></div><span id="25462"></span><div id="comment-25462" class="comment"><div id="post-25462-score" class="comment-score"></div><div class="comment-text"><p>I want do a search based on the content of "Info",last column in the top-most display pane. Search on the basis of packet-list returns null, while on the basis of packet details do point at corresponding packet. Why is it so?.</p></div><div id="comment-25462-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:34)</span> sunshine</div></div><span id="25463"></span><div id="comment-25463" class="comment"><div id="post-25463-score" class="comment-score"></div><div class="comment-text"><p>Searching in the packet-list works for me (version 1.10.0 and 1.8.7). Do you want to search in the packet list (find the next listed packet that matches the search criteria) or do you want to filter the packet list (limit the list of packets to only those that match your search criteria).</p><p>In case of filtering, the "info" column is a constructed column for which there is no filterable field. In general, all the info in the "info" column is also available in specific protocol fields.</p><p>Can you post an image of the packet-list and packet details of your custom dissector and indicate what you would like to search on?</p></div><div id="comment-25463-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:48)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-25429" class="comment-tools"></div><div class="clear"></div><div id="comment-25429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25457"></span>

<div id="answer-container-25457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25457-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Where could be the probable defect?</p></blockquote><p>There is no defect in Wireshark. You can simply search in different views</p><ul><li>Packet list (only the overview of packets with <strong>some</strong> information about the content)</li><li>Packet details (information about dissected fields)</li><li>Packet bytes (the raw packet bytes)</li></ul><p>The results of a search operation are obviously different.</p><p>What are trying to find?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '13, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '13, 03:48</p></div></div><div id="comments-container-25457" class="comments-container"><span id="25458"></span><div id="comment-25458" class="comment"><div id="post-25458-score" class="comment-score"></div><div class="comment-text"><p>Issue is with the custom-dissector, I developed. What I want to do is, perform a search with Packet list, which in my case is returning null.</p></div><div id="comment-25458-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:00)</span> sunshine</div></div><span id="25466"></span><div id="comment-25466" class="comment"><div id="post-25466-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Search on the basis of packet-list returns null, while on the basis of packet details do point at corresponding packet. Why is it so?.</p></blockquote><p>Do you see the search string in the packet list columns (especially the info column)?</p><p>Can you post a screenshot and highlight the search string in the packet list, or post a capture file (probably useless without the dissector)</p></div><div id="comment-25466-info" class="comment-info"><span class="comment-age">(01 Oct '13, 05:23)</span> Kurt Knochner ♦</div></div><span id="25574"></span><div id="comment-25574" class="comment"><div id="post-25574-score" class="comment-score"></div><div class="comment-text"><p>Yes, I can see the string in Info column. Unable to upload screenshot due to policies at workplace.</p></div><div id="comment-25574-info" class="comment-info"><span class="comment-age">(02 Oct '13, 22:21)</span> sunshine</div></div></div><div id="comment-tools-25457" class="comment-tools"></div><div class="clear"></div><div id="comment-25457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


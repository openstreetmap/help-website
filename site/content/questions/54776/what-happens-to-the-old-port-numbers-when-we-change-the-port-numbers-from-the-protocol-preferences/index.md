+++
type = "question"
title = "What happens to the old port numbers when we change the port numbers from the protocol preferences"
description = '''Hi, I am creating dissectors for some proprietary protocols in which I have added preference to specify the port numbers for the dissector. Apart from that I have also registered my dissector to some well known port numbers. My question is that what would happen to the port numbers on which the diss...'''
date = "2016-08-12T09:34:00Z"
lastmod = "2016-08-17T13:28:00Z"
weight = 54776
keywords = [ "lua", "dissector", "wireshark" ]
aliases = [ "/questions/54776" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What happens to the old port numbers when we change the port numbers from the protocol preferences](/questions/54776/what-happens-to-the-old-port-numbers-when-we-change-the-port-numbers-from-the-protocol-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54776-score" class="post-score" title="current number of votes">0</div><span id="post-54776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am creating dissectors for some proprietary protocols in which I have added preference to specify the port numbers for the dissector. Apart from that I have also registered my dissector to some well known port numbers. My question is that what would happen to the port numbers on which the dissector is registered by default by me (in the lua script) if I go to the dissector preference and change the port numbers from there.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '16, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p><span>shobhit_garg91</span><br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div></div><div id="comments-container-54776" class="comments-container"></div><div id="comment-tools-54776" class="comment-tools"></div><div class="clear"></div><div id="comment-54776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54777"></span>

<div id="answer-container-54777" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54777-score" class="post-score" title="current number of votes">0</div><span id="post-54777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Every registration in a dissector table has to be explicitly add and removed. The usual pattern is to get the preference (or default value). and register that. When the preference chances you have to remove the previous registration and put the new one in. There are enough examples of this for the UDP and TCP dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '16, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '16, 11:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-54777" class="comments-container"><span id="54924"></span><div id="comment-54924" class="comment"><div id="post-54924-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy, Thanks for your inputs. I am dealing with the issue of removing the ports that the dissector is registered to. I know that i can use remove() to remove the dissector from specific port numbers. I wanted to know if there is any way in which I could remove my dissector from all the registered ports and then re-register the dissector based on the port numbers specified by the user in preferences section. Please let me know if there is anything I could do in this regards. The major issue is that I have created multiple dissectors, and I need to change the port numbers which they listen to dynamically (from preferences). I am able to add preferences and listen to change in preferences using the PROTOCOL.prefs_changed(). I want remove all the port numbers the dissector was registered for previously and register the protocol to the new port numbers specified in the preferences.</p><p>Thanks.</p></div><div id="comment-54924-info" class="comment-info"><span class="comment-age">(17 Aug '16, 11:43)</span> <span class="comment-user userinfo">shobhit_garg91</span></div></div><span id="54926"></span><div id="comment-54926" class="comment"><div id="post-54926-score" class="comment-score"></div><div class="comment-text"><p>First, all tributes belong to <span>@Jaap</span>, not to me - I have just slightly clarified his original wording.</p><p>I don't know any "drop the whole dissector table contents" method, but is not really clear to me why would you need to generally deactivate the original dissectors which are not in conflict with your assignment of the ports. I mean, if your protocol uses TCP port 23, you need to replace the corresponding row in <code>tcp.port</code> dissector table, but if it doesn't, why should you disable processing of telnet if it is not in conflict with your use of the port?</p><p>So my approach would be to replace only the mappings for those ports which I need to modify, and even to remember the original mapping for each of them so that I could restore it to the table e.g. if I find out that I've chosen that port number for my protocol by mistake.</p></div><div id="comment-54926-info" class="comment-info"><span class="comment-age">(17 Aug '16, 13:04)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54927"></span><div id="comment-54927" class="comment"><div id="post-54927-score" class="comment-score"></div><div class="comment-text"><p>OK, I see your point now after reading <a href="https://ask.wireshark.org/questions/54919/is-there-a-way-to-specify-hierarchy-while-declaring-dissectors-in-wireshark-in-initlua">your other question</a>. For TCP it is normally assumed that high port numbers are used as ephemeral ones, and low ports are "well known" ones, so this type of conflict doesn't happen.</p><p>Wireshark uses a preference "try heuristic dissectors first" which suggests that it can offer the same piece of data to another dissector if the first one couldn't dissect them. So to implement the hierarchy, each of your dissectors has to check both the source and the destination port number, and if it finds out that such combination favours another dissector, do nothing and return 0 to indicate that to the invoking dissector, which will then try the next dissector based on match of the other port number. This, inevitably, requires chaining of existing dissectors with such detectors (so that the telnet dissector from my example above would only be allowed to do its job if no higher priority dissector matches the other port of that packet).</p></div><div id="comment-54927-info" class="comment-info"><span class="comment-age">(17 Aug '16, 13:28)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-54777" class="comment-tools"></div><div class="clear"></div><div id="comment-54777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


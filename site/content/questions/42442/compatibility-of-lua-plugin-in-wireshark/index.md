+++
type = "question"
title = "Compatibility of lua plugin in wireshark?"
description = '''Currently, I have developed my own plugin in lua.In that plugin I have developed my own protocol and dissection using lua APIs(5.2).currently it is working fine and compatible with wireshark version 1.12.5 but I have to provide forward compatibility. Can anyone tell me upto which wireshark version i...'''
date = "2015-05-16T12:01:00Z"
lastmod = "2015-06-29T20:41:00Z"
weight = 42442
keywords = [ "lua", "plugin", "compatibility", "wireshark" ]
aliases = [ "/questions/42442" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Compatibility of lua plugin in wireshark?](/questions/42442/compatibility-of-lua-plugin-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42442-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently, I have developed my own plugin in lua.In that plugin I have developed my own protocol and dissection using lua APIs(5.2).currently it is working fine and compatible with wireshark version 1.12.5 but I have to provide forward compatibility. Can anyone tell me upto which wireshark version it will be supported??</p></div><div id="question-tags" class="tags-container tags">lua plugin compatibility wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '15, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-42442" class="comments-container"></div><div id="comment-tools-42442" class="comment-tools"></div><div class="clear"></div><div id="comment-42442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42459"></span>

<div id="answer-container-42459" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42459-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone tell me upto which wireshark version it will be supported??</p></blockquote><p>No, I don't think so, because there is no official roadmap and no guarantee at all, that the code interfaces will stay untouched for a certain amount of releases. If it's necessary to implement new functionality, the code interface will change and it's up to you, to adjust your code to those changes.</p><p>So, if you want your plugin to work for a defined amout of time, you could ship a certain version of Wireshark alongside with your plugin as a package. As long as you adhere to the GPL, that's no problem, even for commercial products.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '15, 06:30</p></div></div><div id="comments-container-42459" class="comments-container"><span id="42466"></span><div id="comment-42466" class="comment"><div id="post-42466-score" class="comment-score"></div><div class="comment-text"><p>thanks kurt</p></div><div id="comment-42466-info" class="comment-info"><span class="comment-age">(17 May '15, 09:50)</span> ankit</div></div></div><div id="comment-tools-42459" class="comment-tools"></div><div class="clear"></div><div id="comment-42459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43696"></span>

<div id="answer-container-43696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43696-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Kurt's answer is right, but we do try to keep the Lua API backward compatible as much as possible in future releases. For example, if you wrote one that worked in 1.8, the odds are extremely good it will still work in 1.10 and 1.12. I only know of two plugins that didn't continue to work, and that was because we fixed bugs in Wireshark that the old plugins relied on continuing to be bugs - and it was easy to fix the plugins and make them work again.</p><p>For the future release 2.0, as it stands right now the only things that won't continue to work are GUI-specific Lua API functions, such as creating a menu item, using a text-window, dialog box, etc. Those will continue to work in the GTK-based Wireshark GUI, but the Qt-based GUI does not have them for Lua yet so that won't work. I'm hoping we get that working before 2.0 is released.</p><p>Also, if you'd like to improve the chances of it working in the future, you could submit an enhancement bug and attach your Lua plugin along with a capture file that exercises it, to <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a>, and I'll add it to the test suite.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43696" class="comments-container"><span id="43700"></span><div id="comment-43700" class="comment"><div id="post-43700-score" class="comment-score"></div><div class="comment-text"><p>Thanks Handriel for your response.I will try my best to improve in lua as you suggested.</p></div><div id="comment-43700-info" class="comment-info"><span class="comment-age">(29 Jun '15, 22:07)</span> ankit</div></div></div><div id="comment-tools-43696" class="comment-tools"></div><div class="clear"></div><div id="comment-43696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42818"></span>

<div id="answer-container-42818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42818-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use <strong>_VERSION</strong> to get the version of LUA that Wireshark is using and act accordingly.<br />
for example print(_VERSION) will return "Lua 5.2".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/6a8427ead4bf3634030701b9ba9940af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amine%20Ahd&#39;s gravatar image" /><p>Amine Ahd<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amine Ahd has one accepted answer">33%</span> </br></p></div></div><div id="comments-container-42818" class="comments-container"></div><div id="comment-tools-42818" class="comment-tools"></div><div class="clear"></div><div id="comment-42818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


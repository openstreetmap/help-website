+++
type = "question"
title = "From PCAP to SQL"
description = '''I fill an SQL DB with results from a Lua script launched by tshark like eth.src, dhcp.hostname, etc ... I tried to do all in Lua, but wasn&#x27;t successful on the SQL part, reinventing the wheel so I used Python to insert/update data into DB. For the moment, I&#x27;m using a CSV file as an intermediary: Lua ...'''
date = "2015-11-08T21:43:00Z"
lastmod = "2016-04-28T14:14:00Z"
weight = 47420
keywords = [ "python", "lua" ]
aliases = [ "/questions/47420" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [From PCAP to SQL](/questions/47420/from-pcap-to-sql)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47420-score" class="post-score" title="current number of votes">0</div><span id="post-47420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I fill an SQL DB with results from a Lua script launched by tshark like eth.src, dhcp.hostname, etc ... I tried to do all in Lua, but wasn't successful on the SQL part, reinventing the wheel so I used Python to insert/update data into DB.</p><p>For the moment, I'm using a CSV file as an intermediary: Lua parses the whole PCAP, creates a CSV file, and a Python script updates CSV to SQL. The whole is managed by a bash script, it's a bit heavy and not really efficient with so many scripts to handle.</p><p>Is there a better way to communicated between those two languages like socket / pipe / output? What would be more efficient alternatives to fill such SQL DB from PCAP?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-47420" class="comments-container"></div><div id="comment-tools-47420" class="comment-tools"></div><div class="clear"></div><div id="comment-47420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47440"></span>

<div id="answer-container-47440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47440-score" class="post-score" title="current number of votes">1</div><span id="post-47440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a better way to communicated between those two languages like socket / pipe / output?</p></blockquote><p>Why are you using the Lua script at all? You could run tshark and parse the output with python (which then adds data to the database).</p><blockquote><p>tshark -nr input.pcap -Y "dhcp" -T fields -e eth.src -e eth.dst -e ip.src -ip.dst -e dhcp.hostname -E header=y -E separator=; | python yourscript.py</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '15, 14:41</strong> </span></p></div></div><div id="comments-container-47440" class="comments-container"><span id="47459"></span><div id="comment-47459" class="comment"><div id="post-47459-score" class="comment-score"></div><div class="comment-text"><p>I use Lua to retrieve hexa values of some filters like "wlan_mgt.ssid" if some non ASCII chars are printed, like explained in <a href="https://ask.wireshark.org/questions/43521/retrieve-hex-values-in-lua">https://ask.wireshark.org/questions/43521/retrieve-hex-values-in-lua</a></p><p>Can you get such hexa values with tshark -T fields?</p></div><div id="comment-47459-info" class="comment-info"><span class="comment-age">(10 Nov '15, 00:39)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div><span id="47464"></span><div id="comment-47464" class="comment"><div id="post-47464-score" class="comment-score">1</div><div class="comment-text"><p>In that case you could use '-T pdml' or '-T psml' instead of '-T fields' and parse the XML like structure, which 'should' contain hex values as well. If that does not work, you can still go the 'brute force' route with</p><blockquote><p>tshark -nr input.pcap -Vx | python script.py</p></blockquote><p>And if that does not contain the values in HEX, your Lua/Python mix is probably the best option already ;-)</p><p>Maybe you can drop the bash script and call tshark (with the Lua script parameters) directly from your python script...</p><p>Regards<br />
Kurt</p></div><div id="comment-47464-info" class="comment-info"><span class="comment-age">(10 Nov '15, 04:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="52025"></span><div id="comment-52025" class="comment"><div id="post-52025-score" class="comment-score"></div><div class="comment-text"><p>PyShark could be another option, information regarding it can be found here: <a href="http://kiminewt.github.io/pyshark/">http://kiminewt.github.io/pyshark/</a></p></div><div id="comment-52025-info" class="comment-info"><span class="comment-age">(27 Apr '16, 15:24)</span> <span class="comment-user userinfo">kim</span></div></div></div><div id="comment-tools-47440" class="comment-tools"></div><div class="clear"></div><div id="comment-47440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52062"></span>

<div id="answer-container-52062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52062-score" class="post-score" title="current number of votes">0</div><span id="post-52062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I use tshark to export to csv. The "pandas" library can then load the csv (pandas.read_csv)and export it to sql (pandas.write_sql IIRC ?). This might be more efficient then your current script depending on how you convert things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '16, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/e2e55c6d8b33c6f22b441b0f39cfa209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teto&#39;s gravatar image" /><p><span>teto</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teto has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52062" class="comments-container"></div><div id="comment-tools-52062" class="comment-tools"></div><div class="clear"></div><div id="comment-52062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Wireshark and SQL"
description = '''Hello! Is wireshark able to decode ms sql queries? (sql 2005 server). With mysql - no problems:   tshark -i lo -d tcp.port==3306,mysql -T fields -e mysql.query  But for SQl there is no smth like &quot;tcp.port==1433,mssql&quot; and &quot;fields -e mssql.query&quot;. Or it doesn&#x27;t work with TDS packets? I just need to e...'''
date = "2017-10-23T05:53:00Z"
lastmod = "2017-10-23T06:02:00Z"
weight = 64103
keywords = [ "tds", "decrypt", "sql" ]
aliases = [ "/questions/64103" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and SQL](/questions/64103/wireshark-and-sql)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64103-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! Is wireshark able to decode ms sql queries? (sql 2005 server). With mysql - no problems:</p><blockquote><p>tshark -i lo -d tcp.port==3306,mysql -T fields -e mysql.query</p></blockquote><p>But for SQl there is no smth like "tcp.port==1433,mssql" and "fields -e mssql.query". Or it doesn't work with TDS packets? I just need to extract clear SQL-queries from traffic...</p></div><div id="question-tags" class="tags-container tags">tds decrypt sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/51a92fe03eb10523cb90fc59a5546dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alex31337&#39;s gravatar image" /><p>alex31337<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alex31337 has no accepted answers">0%</span></p></div></div><div id="comments-container-64103" class="comments-container"></div><div id="comment-tools-64103" class="comment-tools"></div><div class="clear"></div><div id="comment-64103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64104"></span>

<div id="answer-container-64104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64104-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol used by MS SQL Server is TDS, so all filter fields are "tds.xxx" rather than "mssql"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64104" class="comments-container"><span id="64105"></span><div id="comment-64105" class="comment"><div id="post-64105-score" class="comment-score"></div><div class="comment-text"><p>So, it will be: tshark -i lo -d tcp.port==1433,tds -T fields -e tds.query ???</p></div><div id="comment-64105-info" class="comment-info"><span class="comment-age">(23 Oct '17, 06:05)</span> alex31337</div></div><span id="64106"></span><div id="comment-64106" class="comment"><div id="post-64106-score" class="comment-score"></div><div class="comment-text"><p>You shouldn't need the <code>-d tcp.port==1433,tds</code> as the tds dissector already registers for that port.</p><p>There is a <code>tds.query</code> field, but the comment next to it says "SQLBatch Stream", so it may or may not do what you want.</p></div><div id="comment-64106-info" class="comment-info"><span class="comment-age">(23 Oct '17, 06:38)</span> grahamb ♦</div></div><span id="64107"></span><div id="comment-64107" class="comment"><div id="post-64107-score" class="comment-score"></div><div class="comment-text"><p>And where can I find list of available fields? (their correct syntax)</p></div><div id="comment-64107-info" class="comment-info"><span class="comment-age">(23 Oct '17, 06:44)</span> alex31337</div></div><span id="64108"></span><div id="comment-64108" class="comment"><div id="post-64108-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.wireshark.org/docs/dfref/t/tds.html">https://www.wireshark.org/docs/dfref/t/tds.html</a></p></div><div id="comment-64108-info" class="comment-info"><span class="comment-age">(23 Oct '17, 06:47)</span> alex31337</div></div><span id="64109"></span><div id="comment-64109" class="comment"><div id="post-64109-score" class="comment-score"></div><div class="comment-text"><p>Or <code>tshark -G fields</code>, although that doesn't limit to a particular dissector, or show version ranges.</p></div><div id="comment-64109-info" class="comment-info"><span class="comment-age">(23 Oct '17, 07:27)</span> grahamb ♦</div></div><span id="64110"></span><div id="comment-64110" class="comment not_top_scorer"><div id="post-64110-score" class="comment-score"></div><div class="comment-text"><p>But anyway, IT'S POSSIBLE to grab pure MS sql-queries (that clients send to server) via Tshark, is it right? (traffic not encrypted, only TDS)</p></div><div id="comment-64110-info" class="comment-info"><span class="comment-age">(23 Oct '17, 07:47)</span> alex31337</div></div><span id="64112"></span><div id="comment-64112" class="comment not_top_scorer"><div id="post-64112-score" class="comment-score"></div><div class="comment-text"><p>Presumably, hence the inclusion of a TDS dissector.</p></div><div id="comment-64112-info" class="comment-info"><span class="comment-age">(23 Oct '17, 08:35)</span> grahamb ♦</div></div><span id="64114"></span><div id="comment-64114" class="comment not_top_scorer"><div id="post-64114-score" class="comment-score"></div><div class="comment-text"><blockquote><p>.....-T fields -e tds.query WARNING **: 'tds.query' isn't a valid field!</p></blockquote><p>WTF!?</p></div><div id="comment-64114-info" class="comment-info"><span class="comment-age">(23 Oct '17, 09:57)</span> alex31337</div></div><span id="64119"></span><div id="comment-64119" class="comment not_top_scorer"><div id="post-64119-score" class="comment-score"></div><div class="comment-text"><p>Works for me (as in doesn't show an error). What version of tshark?</p><p>If I induce an error I get this kind of output:</p><pre><code>&gt; tshark.exe -r capture.pcapng -T fields -e tds.2query
tshark: Some fields aren&#39;t valid:
        tds.2query</code></pre></div><div id="comment-64119-info" class="comment-info"><span class="comment-age">(23 Oct '17, 11:31)</span> grahamb ♦</div></div><span id="64121"></span><div id="comment-64121" class="comment not_top_scorer"><div id="post-64121-score" class="comment-score"></div><div class="comment-text"><p>TShark 1.12.1</p></div><div id="comment-64121-info" class="comment-info"><span class="comment-age">(23 Oct '17, 11:51)</span> alex31337</div></div><span id="64123"></span><div id="comment-64123" class="comment not_top_scorer"><div id="post-64123-score" class="comment-score"></div><div class="comment-text"><p>I've updated to 2.4.2, now "-T fields -e tds.query" doesnt print error! But I see no SQL-instructions, but blank lines -( Can you see SELECT,INSERT, UPDATE etc after you print "tshark.exe -r capture.pcapng -T fields -e tds.query"?</p></div><div id="comment-64123-info" class="comment-info"><span class="comment-age">(23 Oct '17, 12:27)</span> alex31337</div></div><span id="64124"></span><div id="comment-64124" class="comment not_top_scorer"><div id="post-64124-score" class="comment-score"></div><div class="comment-text"><p>That's <a href="https://wiki.wireshark.org/Development/LifeCycle">EOL-ed over a year ago</a>. Please find a way to upgrade.</p></div><div id="comment-64124-info" class="comment-info"><span class="comment-age">(23 Oct '17, 12:29)</span> Jaap ♦</div></div><span id="64125"></span><div id="comment-64125" class="comment not_top_scorer"><div id="post-64125-score" class="comment-score"></div><div class="comment-text"><p>Without seeing your actual file, it is just guessing, but could it be that you have also other than <code>tds</code> packets in the file? If so, add a display filter <code>-Y tds.query</code> to your command line, so that other packets are not displayed. For packets which don't contain a required field, tshark prints a blank line.</p></div><div id="comment-64125-info" class="comment-info"><span class="comment-age">(23 Oct '17, 12:54)</span> sindy</div></div><span id="64126"></span><div id="comment-64126" class="comment not_top_scorer"><div id="post-64126-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned, the comment in the code next to tds.query mentions "SQL Batch Stream", so I'm not sure if the field shows all SQL query strings.</p><p>I don't have a tds capture to test. maybe you can share one with us to help out?</p></div><div id="comment-64126-info" class="comment-info"><span class="comment-age">(23 Oct '17, 13:53)</span> grahamb ♦</div></div></div><div id="comment-tools-64104" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-64104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


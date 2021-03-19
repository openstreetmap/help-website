+++
type = "question"
title = "Mystery...protocol and speed depend on how long you wait to query"
description = '''Help please. The Situation: Eight identical Dell computers (1 yr old) with Windows 7 Pro SP1 connected via an HP switch (all wired) and sharing via a homegroup. There is one shared folder on Computer &#x27;S&#x27; containing a commonly queried file, no person sits at or works on Computer &#x27;S&#x27;, and the query so...'''
date = "2017-02-15T15:27:00Z"
lastmod = "2017-02-17T12:07:00Z"
weight = 59445
keywords = [ "waittime", "smb2", "tcp" ]
aliases = [ "/questions/59445" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mystery...protocol and speed depend on how long you wait to query](/questions/59445/mysteryprotocol-and-speed-depend-on-how-long-you-wait-to-query)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59445-score" class="post-score" title="current number of votes">0</div><span id="post-59445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Help please. The Situation: Eight identical Dell computers (1 yr old) with Windows 7 Pro SP1 connected via an HP switch (all wired) and sharing via a homegroup. There is one shared folder on Computer 'S' containing a commonly queried file, no person sits at or works on Computer 'S', and the query software prevents any 2 people from querying the file at the same time (ie. no overlapping queries).</p><p>The Problem: If no-one queries that file from their computer for 15 seconds or more, then the next person to query it from any computer will receive their results back fast (&lt;2 sec), and the Wireshark capture indicates that most packets are like: TCP 1514 [TCP segment of a reassembled PDU]</p><p>However, in the 15 seconds after someone queries the file, one of two things happens: 1) If the same person (same computer) re-queries the database (with the same or different query) inside 15 seconds, they will get fast results again (&lt;2 sec) with TCP and 1514 Lengths just as above. But... 2) If anyone else (a second person at a second computer) queries the database in less than 15 seconds, they will get slow results (&gt;20 seconds), and Wireshark captures frame pairs like: SMB2 191 Read Request Len:1024 Off:24194048 File: S Drive\database.xyz SMB2 1182 Read Response If this second person sits and waits for 15 seconds instead of placing the query right away, then they will again have a fast response (&lt;2 sec) and will have frames again like "TCP 1514 [TCP segment of a reassembled PDU]".</p><p>Unfortunately, making each person wait 15 seconds since the last person's query is not feasible. We need to place queries every 5-10 seconds, and we need them to all be fast. As things are now, if we keep placing queries every 5-10 seconds apart, then the 15 seconds of wait time never passes, so all the queries take &gt;20 seconds.</p><p>The problem is like a swinging "bridge"... if it's pointed to your computer, you get fast queries. But unless anyone else waits 15 seconds after your last query for the bridge to "free up", they will get a slow response. (Again, 2 overlapping queries is not possible; all queries are place sequentially.) I suspect that Windows 7 is enforcing a policy that selects TCP via IPv6 for the first query (fast), and then it selects SMB2 and NetBios (slow) for any other subsequent queries, unless 15 seconds is allowed to lapse from the end of the last query (either TCP or SMB2); the 15 seconds seems to allow it to go back to TCP. I've searched for documentation of such a Windows behavior, but can't find it, nor have I found any way to affect this behavior. But I'm pretty clueless, so I'd really appreciate any ideas you all have. Thank you for your consideration. I'd be happy to include more details from the Wireshark captures if it would be helpful.</p><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-waittime" rel="tag" title="see questions tagged &#39;waittime&#39;">waittime</span> <span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/1a1bd6b83b8951d551806872cfe5dd3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hitched01&#39;s gravatar image" /><p><span>Hitched01</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hitched01 has no accepted answers">0%</span></p></div></div><div id="comments-container-59445" class="comments-container"><span id="59465"></span><div id="comment-59465" class="comment"><div id="post-59465-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>I suspect that Windows 7 is enforcing a policy that selects TCP via IPv6 for the first query (fast), and then it selects SMB2 and NetBios (slow) for any other subsequent queries, unless 15 seconds is allowed to lapse from the end of the last query (either TCP or SMB2)</p></blockquote></blockquote><p>This probably is not your root cause but a packet trace would prove it either way. You will likely have better luck if you post a sanitized trace which shows the two cases: fast and slow, for comparison.</p></div><div id="comment-59465-info" class="comment-info"><span class="comment-age">(16 Feb '17, 03:26)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="59489"></span><div id="comment-59489" class="comment"><div id="post-59489-score" class="comment-score"></div><div class="comment-text"><p>Bob, thank you for taking a look. I will do as you suggest.</p></div><div id="comment-59489-info" class="comment-info"><span class="comment-age">(16 Feb '17, 21:33)</span> <span class="comment-user userinfo">Hitched01</span></div></div><span id="59509"></span><div id="comment-59509" class="comment"><div id="post-59509-score" class="comment-score"></div><div class="comment-text"><p>Below are the beginnings and endings of traces for a Slow (&gt;20 sec) query, and then a Fast one (&lt;2 sec). Intervening lines basically repeat those immediately before. When a query is placed, the querying program changes the status of a lockfile (LockFile.Stm) to locked, and then queries Database.xyz. When the query results are all returned, the LockFile.Stm file is unlocked. Both of the queries below were placed on the same machine, same query. The slow query was placed within 15 seconds of another computer completing a query; the fast query was placed more than 15 seconds after completion of a prior query by another computer. Thank you for taking a look at this issue. Please let me know if you need more info. I'm sorry if this doesn't look readable when pasted on-site (but it should look readable in notepad, etc). I appreciate your expertise.</p><p>Slow Query:</p><hr /><p>0 192.168.1.16 192.168.1.10 BJNP 174 Scanner Command: Scan Job Details<br />
0.00371 192.168.1.10 192.168.1.16 BJNP 110 Scanner Response: Scan Job Details<br />
0.602226 HewlettP_76:e8:cd Spanning-tree-(for-bridges)_00 STP 64 RST. Root = 32768/0/78:48:59:76:e8:bc Cost = 0 Port = 0x8010 1.491427 fe80::216c:a17e:e377:3737 ff02::1:ff2f:d1a6 ICMPv6 86 Neighbor Solicitation for fe80::8013:e10e:132f:d1a6 from f8:bc:12:a3:e7:69<br />
1.492367 fe80::8013:e10e:132f:d1a6 ff02::1:ff77:3737 ICMPv6 86 Neighbor Solicitation for fe80::216c:a17e:e377:3737 from 48:4d:7e:d2:d6:03<br />
1.492546 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 310 Create Request File: LockFile.Stm<br />
1.492697 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 ICMPv6 86 Neighbor Advertisement fe80::216c:a17e:e377:3737 (sol, ovr) is at f8:bc:12:a3:e7:69<br />
1.493115 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 ICMPv6 86 Neighbor Advertisement fe80::8013:e10e:132f:d1a6 (sol, ovr) is at 48:4d:7e:d2:d6:03<br />
1.493413 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: LockFile.Stm<br />
1.494088 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
1.494831 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
1.495464 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 294 Create Request File:<br />
1.49629 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: [unknown]<br />
1.497309 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request File: [unknown] SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.498111 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.49845 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: [unknown]<br />
1.499116 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
1.500463 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 366 Create Request File: LockFile.Stm<br />
1.501508 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_PENDING<br />
1.502607 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 406 Create Response File: LockFile.Stm<br />
1.502957 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=1057 Ack=1348 Win=63453 Len=0<br />
1.505197 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.5061 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.507581 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.508448 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.509642 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.510654 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.511788 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.512676 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.513118 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.514037 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.514532 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
1.51542 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
1.515856 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: LockFile.Stm<br />
1.51673 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 350 Create Response File: LockFile.Stm<br />
1.516843 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 214 SetInfo Request FILE_INFO/SMB2_FILE_BASIC_INFO File: LockFile.Stm<br />
1.517631 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 144 SetInfo Response<br />
1.517717 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
1.518401 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
1.522844 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 210 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: Database.xyz<br />
1.523635 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 280 Find Response<br />
1.52397 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 210 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: Database.xyz<br />
1.524838 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 280 Find Response<br />
1.525012 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 326 Create Request File: Database.xyz<br />
1.525798 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: Database.xyz<br />
1.525926 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: Database.xyz<br />
1.526596 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
1.526909 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 382 Create Request File: Database.xyz<br />
1.535321 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_PENDING<br />
1.535757 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 406 Create Response File: Database.xyz<br />
1.535796 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3225 Ack=4179 Win=63607 Len=0<br />
1.536055 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:0<br />
1.536532 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
1.536532 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
1.536575 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3342 Ack=7059 Win=64800 Len=0<br />
1.536774 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
1.536936 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.537533 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.537602 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.53819 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.538257 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.53879 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.538931 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: Database.xyz-journal<br />
1.539631 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND<br />
1.539777 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 334 Create Request File: Database.xyz-wal<br />
1.540467 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND<br />
1.540564 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:0<br />
1.541231 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.541328 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:5120<br />
1.542038 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.542171 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:6144<br />
1.542883 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.54339 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.544088 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.544529 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.545244 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.545788 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.546512 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.546793 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.547494 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.548254 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:16 Off:24<br />
1.549053 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 174 Read Response<br />
1.550448 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.551241 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.552581 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.553376 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.553791 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.554563 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.554922 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
1.555699 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
1.556667 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:16 Off:24<br />
1.557505 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 174 Read Response<br />
1.558482 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:1024<br />
1.559341 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.55992 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:14023680<br />
1.560761 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.561336 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:159744<br />
1.562129 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.562593 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:9216<br />
1.563352 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.563743 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:10240<br />
1.564546 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.565323 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:11264<br />
1.566155 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.56668 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:13312<br />
1.56748 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.56792 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:14336<br />
1.568749 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.569348 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:15360<br />
1.570221 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
1.570818 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:16384<br />
1.571659 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response</p><p><em>These lines repeat...</em></p><p>29.293982 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:37540864<br />
29.294546 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.294806 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:37543936<br />
29.295317 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.295429 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:37547008<br />
29.295939 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.296068 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:35646464<br />
29.29659 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.296717 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:37550080<br />
29.297226 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.297351 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:1024 Off:37552128<br />
29.297865 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1182 Read Response<br />
29.298043 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 190 Lock Request<br />
29.298514 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 146 Lock Response<br />
29.301568 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 310 Create Request File: LockFile.Stm<br />
29.302166 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: LockFile.Stm<br />
29.30244 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
29.30286 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
29.303088 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 294 Create Request File:<br />
29.303566 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: [unknown]<br />
29.303846 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request File: [unknown] SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.304357 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.304484 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: [unknown]<br />
29.304871 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
29.3054 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 366 Create Request File: LockFile.Stm<br />
29.306406 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 406 Create Response File: LockFile.Stm<br />
29.307448 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.308262 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.308961 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.309661 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.311094 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.311869 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.312917 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.313896 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.314766 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.315715 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.316174 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
29.317088 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
29.317726 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: LockFile.Stm<br />
29.318611 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 350 Create Response File: LockFile.Stm<br />
29.318841 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 214 SetInfo Request FILE_INFO/SMB2_FILE_BASIC_INFO File: LockFile.Stm<br />
29.319757 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 144 SetInfo Response<br />
29.319979 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
29.320639 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
29.528953 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3947161 Ack=37317865 Win=63744 Len=0<br />
29.571593 fe80::8013:e10e:132f:d1a6 ff02::1:2 DHCPv6 147 Solicit XID: 0x7d7f2d CID: 000100011fbdca93484d7ed2d603<br />
29.790336 192.168.1.1 255.255.255.255 UDP 215 32771 â†’ 7423 Len=173<br />
30.601115 HewlettP_76:e8:cd Spanning-tree-(for-bridges)_00 STP 64 RST. Root = 32768/0/78:48:59:76:e8:bc Cost = 0 Port = 0x8010 32.073016 192.168.1.16 192.168.1.10 BJNP 174 Scanner Command: Scan Job Details<br />
32.078859 192.168.1.10 192.168.1.16 BJNP 110 Scanner Response: Scan Job Details<br />
32.601157 HewlettP_76:e8:cd Spanning-tree-(for-bridges)_00 STP 64 RST. Root = 32768/0/78:48:59:76:e8:bc Cost = 0 Port = 0x8010 32.664384 Dell_a3:e7:69 Canon_b5:d0:c5 ARP 42 Who has 192.168.1.10? Tell 192.168.1.16<br />
32.665461 Canon_b5:d0:c5 Dell_a3:e7:69 ARP 60 192.168.1.10 is at 88:87:17:b5:d0:c5<br />
<strong><em><em></em></em></strong><em><strong><em><strong>End Slow Query</strong></em><strong><em>*</em></strong></strong></em></p><em></em><p>Fast Query:</p><hr /><p>60.13671 192.168.1.16 192.168.1.10 BJNP 174 Scanner Command: Scan Job Details<br />
60.140568 192.168.1.10 192.168.1.16 BJNP 110 Scanner Response: Scan Job Details<br />
60.389343 192.168.1.1 255.255.255.255 UDP 215 32771 â†’ 7423 Len=173<br />
60.600059 HewlettP_76:e8:cd Spanning-tree-(for-bridges)_00 STP 64 RST. Root = 32768/0/78:48:59:76:e8:bc Cost = 0 Port = 0x8010 61.152912 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 310 Create Request File: LockFile.Stm<br />
61.153778 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: LockFile.Stm<br />
61.154021 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
61.154699 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
61.154987 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 294 Create Request File:<br />
61.155784 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: [unknown]<br />
61.155971 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request File: [unknown] SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.156715 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.15685 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: [unknown]<br />
61.15752 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
61.157905 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 366 Create Request File: LockFile.Stm<br />
61.159091 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 406 Create Response File: LockFile.Stm<br />
61.159495 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.160383 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.160633 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.161501 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.161759 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.162623 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.16309 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.163949 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.16427 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.165148 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.166771 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
61.167731 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
61.168023 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: LockFile.Stm<br />
61.168894 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 350 Create Response File: LockFile.Stm<br />
61.169256 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 214 SetInfo Request FILE_INFO/SMB2_FILE_BASIC_INFO File: LockFile.Stm<br />
61.170151 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 144 SetInfo Response<br />
61.170609 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
61.171356 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
61.176831 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 210 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: Database.xyz<br />
61.177721 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 280 Find Response<br />
61.178054 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 210 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: Database.xyz<br />
61.178909 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 280 Find Response<br />
61.179067 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 326 Create Request File: Database.xyz<br />
61.179828 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 318 Create Response File: Database.xyz<br />
61.180126 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: Database.xyz<br />
61.180785 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
61.181175 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 382 Create Request File: Database.xyz<br />
61.182321 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 406 Create Response File: File:<br />
61.182485 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:0 File: F<br />
61.183222 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.183223 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.183224 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.183294 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3950686 Ack=37326325 Win=64800 Len=0<br />
61.183523 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: Database.xyz-journal<br />
61.18405 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND<br />
61.184211 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 334 Create Request File: Database.xyz-wal<br />
61.184915 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 151 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND<br />
61.185513 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:4096 File: Database.xyz<br />
61.18619 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.186191 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.186192 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.186248 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3951331 Ack=37330659 Win=64800 Len=0<br />
61.188014 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:14020608 File: Database.xyz<br />
61.188704 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.188709 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.188712 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.18892 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3951448 Ack=37334839 Win=64800 Len=0<br />
61.188984 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:159744 File: Database.xyz<br />
61.189547 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.189548 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.189622 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3951565 Ack=37337719 Win=64800 Len=0<br />
61.189856 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.19008 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:8192 File: Database.xyz<br />
61.190731 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.190732 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.190733 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.190872 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3951682 Ack=37343199 Win=64800 Len=0<br />
61.191053 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:12288 File: Database.xyz<br />
61.191064 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:24576 Off:16384 File: Database.xyz<br />
61.191438 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 74 445 â†’ 49278 [ACK] Seq=37343199 Ack=3951916 Win=64566 Len=0<br />
61.19178 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191781 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191782 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
61.191784 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191784 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191785 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191786 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191786 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191787 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191787 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191788 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191788 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191789 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191789 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.19179 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.191925 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3951916 Ack=37347379 Win=64800 Len=0<br />
61.192037 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192038 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192039 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.19204 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.19204 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192041 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 254 Read Response<br />
61.192041 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:24576 Off:40960 File: Database.xyz<br />
61.192083 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3952033 Ack=37371859 Win=64800 Len=0<br />
61.192907 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192918 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192918 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192919 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.19292 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.19292 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.192921 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.193066 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=3952033 Ack=37382119 Win=64800 Len=0<br />
61.193113 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.193123 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.193124 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.193125 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
61.193126 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
</p><p><em>These lines repeat...</em></p></em><p><em>63.209322 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.209323 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.209375 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=4190830 Ack=75265403 Win=64800 Len=0<br />
63.209566 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
63.210615 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:37076992 File: Database.xyz<br />
63.211195 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.211411 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.211411 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
63.211443 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=4190947 Ack=75270883 Win=64800 Len=0<br />
63.211819 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 191 Read Request Len:4096 Off:37376000 File: Database.xyz<br />
63.212266 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.212473 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 TCP 1514 [TCP segment of a reassembled PDU]<br />
63.212474 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 1374 Read Response<br />
63.2125 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=4191064 Ack=75275063 Win=64800 Len=0<br />
63.217061 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 286 Create Request File: LockFile.Stm<br />
63.217894 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 262 Create Response File: LockFile.Stm<br />
63.218046 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
63.21868 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
63.218977 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.219914 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.220469 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.221329 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.221542 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.22238 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.222563 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.223402 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.223578 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.224401 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.22459 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.225425 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.225601 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 198 Find Request SMB2_FIND_BOTH_DIRECTORY_INFO Pattern: LockFile.Stm<br />
63.226434 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 268 Find Response<br />
63.226557 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 342 Create Request File: LockFile.Stm<br />
63.227364 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 350 Create Response File: LockFile.Stm<br />
63.227434 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 214 SetInfo Request FILE_INFO/SMB2_FILE_BASIC_INFO File: LockFile.Stm<br />
63.228205 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 144 SetInfo Response<br />
63.22826 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 SMB2 166 Close Request File: LockFile.Stm<br />
63.228915 fe80::8013:e10e:132f:d1a6 fe80::216c:a17e:e377:3737 SMB2 202 Close Response<br />
63.442527 fe80::216c:a17e:e377:3737 fe80::8013:e10e:132f:d1a6 TCP 74 49278 â†’ 445 [ACK] Seq=4192736 Ack=75277211 Win=64132 Len=0<br />
63.449145 192.168.1.1 255.255.255.255 UDP 215 32771 â†’ 7423 Len=173<br />
64.145058 192.168.1.16 192.168.1.10 BJNP 174 Scanner Command: Scan Job Details<br />
64.151115 192.168.1.10 192.168.1.16 BJNP 110 Scanner Response: Scan Job Details<br />
<strong><em></em></strong></em><strong><em><strong>End Fast Query</strong></em><strong><em>*</em></strong></strong></p></div><div id="comment-59509-info" class="comment-info"><span class="comment-age">(17 Feb '17, 10:45)</span> <span class="comment-user userinfo">Hitched01</span></div></div></div><div id="comment-tools-59445" class="comment-tools"></div><div class="clear"></div><div id="comment-59445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59514"></span>

<div id="answer-container-59514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59514-score" class="post-score" title="current number of votes">2</div><span id="post-59514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Hitched01</p><p>Your question and the brief traces reveal multiple problems.</p><p><strong>Application Design</strong></p><p>You have a database application and place a file on an SMB share. Multiple clients compete for access to the file. Both file server and application have to make sure, that the file contains valid data at all times.</p><p>SMB offers a feature called "opportunistic locking". Client A can send a Lock Request to the server to signal that he wants exclusive access to a certain region. If client B is holding this lock the server has to send a Lock Request to client B. Client A can only continue, once client B releases the lock. How fast that happens depends on client B. There are situations where the application has to be in a proper state before the lock can be released, like flushing buffers.</p><p>Unfortunately this opportunistic locking only works for a small number of clients: Lock management can put a tremendous load on the server.</p><p>It would be advisable to use a database for this application. "Database" would be something like MS-SQL, MySQL or any similar database that can be reached through a dedicated network port. SQLITE databases do not count, as they are implemented as a file and you have the whole locking game going on.</p><p><strong>Server Performance / Application Behavior</strong></p><p>Your "slow trace" shows that the client is sending a large number of requests, each 1024 byte at a time. Each request is answered within 1 millisecond. But 15.000 times 1 milliseconds still results in a response time of 15 seconds.</p><p>The "fast trace" shows read requests of 24 kByte, where each request is served within 1 millisecond. I wonder if the "fast trace" shows large block sizes as well. In theory, this should complete within 1 second.</p><p>Image you host a party and want order pizza for you and your guests. Within the "slow trace" you order one slice at a time. The next order is only placed after the first slice has been consumed. No wonder it takes all night long until everybody is fed. The "fast trace" orders 24 slices at a time.</p><p>Depending on the number of guests it might still take some time to feed everybody. At least the guests stop raiding your kitchen ...</p><p><strong>Operating System</strong></p><p>Your question mentions that all systems run Windows 7, which is a workstation OS. Workstations are not optimized to run as file servers, while Windows server editions are not optimized for desktop applications.</p><p>If all the tuning and analysis does not help, you might want to consider a test with a Windows Server version.</p><p><strong>Why the small block sizes?</strong></p><p>There are a few possibilities. One point is definitely the application. You might want to talk to your vendor or developer and have them check their code.</p><p>Another option is the server. Since the server uses SMB2 the client needs credits to ask run I/O operations. My first check would be, if the client has sufficient credits.</p><p>I tried to put a few hints into the blog entry <a href="https://blog.packet-foo.com/2016/10/trace-file-case-files-smb2-performance/">Trace File Case Files: SMB2 Performance</a> which Jasper published on his excellent web site <a href="https://blog.packet-foo.com/2016/10/">blog.packet-foo.com</a>.</p><p><strong>And then?</strong></p><p>For a full analysis we need a trace take at the server side. No screen shots or text-listings please.</p><p>Good hunting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span> </br></br></p></div></div><div id="comments-container-59514" class="comments-container"></div><div id="comment-tools-59514" class="comment-tools"></div><div class="clear"></div><div id="comment-59514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>


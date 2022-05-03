CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "core_seriesmodel_genre" (
	"id"	integer NOT NULL,
	"seriesmodel_id"	bigint NOT NULL,
	"genremodel_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("genremodel_id") REFERENCES "core_genremodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("seriesmodel_id") REFERENCES "core_seriesmodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "core_softwaresgamesmodel_genre" (
	"id"	integer NOT NULL,
	"softwaresgamesmodel_id"	bigint NOT NULL,
	"genremodel_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("softwaresgamesmodel_id") REFERENCES "core_softwaresgamesmodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("genremodel_id") REFERENCES "core_genremodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_moviemodel_genre" (
	"id"	integer NOT NULL,
	"moviemodel_id"	bigint NOT NULL,
	"genremodel_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("moviemodel_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("genremodel_id") REFERENCES "core_genremodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_bsubmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_classicmodel" (
	"id"	integer NOT NULL,
	"type"	varchar(50),
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_dualaudiomodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_genremodel" (
	"id"	integer NOT NULL,
	"genre_name"	varchar(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "core_hindidubbedmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_imdbtopmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_jamesbondmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_oscarwinningmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_satyajitraymodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_specialmodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_superheromodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_topslidemodel" (
	"id"	integer NOT NULL,
	"created_at"	datetime NOT NULL,
	"movie_content_id"	bigint,
	"series_content_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("series_content_id") REFERENCES "core_seriesmodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("movie_content_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "dashboard_userdashboardmodule" (
	"id"	integer NOT NULL,
	"title"	varchar(255) NOT NULL,
	"module"	varchar(255) NOT NULL,
	"app_label"	varchar(255),
	"user"	integer unsigned NOT NULL CHECK("user" >= 0),
	"column"	integer unsigned NOT NULL CHECK("column" >= 0),
	"order"	integer NOT NULL,
	"settings"	text NOT NULL,
	"children"	text NOT NULL,
	"collapsed"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "jet_bookmark" (
	"id"	integer NOT NULL,
	"url"	varchar(200) NOT NULL,
	"title"	varchar(255) NOT NULL,
	"user"	integer unsigned NOT NULL CHECK("user" >= 0),
	"date_add"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "jet_pinnedapplication" (
	"id"	integer NOT NULL,
	"app_label"	varchar(255) NOT NULL,
	"user"	integer unsigned NOT NULL CHECK("user" >= 0),
	"date_add"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_summernote_attachment" (
	"id"	integer NOT NULL,
	"name"	varchar(255),
	"file"	varchar(100) NOT NULL,
	"uploaded"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "core_softwaresgamesmodel" (
	"id"	integer NOT NULL,
	"title"	varchar(250),
	"slug"	varchar(250),
	"poster"	varchar(100),
	"thumbnail"	varchar(100),
	"category"	varchar(50),
	"platform"	varchar(50),
	"rated"	varchar(250),
	"size"	varchar(250),
	"release_date"	date,
	"developer"	varchar(250),
	"description"	text,
	"min_sys_req"	text,
	"rec_sys_req"	text,
	"general_notes"	text,
	"gdrive_download_link"	varchar(999),
	"onedrive_download_link"	varchar(999),
	"torrent"	varchar(999),
	"info1"	varchar(250),
	"info2"	varchar(250),
	"created_at"	datetime NOT NULL,
	"direct_download"	varchar(999),
	"created_by_id"	integer,
	"last_update_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("last_update_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("created_by_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_seriesmodel" (
	"id"	integer NOT NULL,
	"title"	varchar(250),
	"slug"	varchar(250),
	"description"	text,
	"poster"	varchar(100),
	"thumbnail"	varchar(100),
	"director"	varchar(250),
	"starring"	varchar(250),
	"type"	varchar(50),
	"release_date"	date,
	"end_date"	date,
	"rating"	real,
	"rated"	varchar(250),
	"trailer_link"	varchar(999),
	"info1"	varchar(250),
	"info2"	varchar(250),
	"synopsys"	text,
	"created_at"	datetime NOT NULL,
	"writers"	varchar(250),
	"tmdb_poster"	varchar(999),
	"tmdb_thumbnail"	varchar(999),
	"created_by_id"	integer,
	"last_update_id"	integer,
	"tmdbid"	bigint UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("last_update_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("created_by_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_moviemodel" (
	"id"	integer NOT NULL,
	"title"	varchar(250),
	"slug"	varchar(250),
	"description"	text,
	"poster"	varchar(100),
	"thumbnail"	varchar(100),
	"director"	varchar(250),
	"starring"	varchar(250),
	"type"	varchar(50),
	"runtime"	varchar(250),
	"rating"	real,
	"rated"	varchar(250),
	"release_date"	date,
	"trailer_link"	varchar(999),
	"gdrive_quality_480p"	varchar(999),
	"gdrive_quality_720p"	varchar(999),
	"gdrive_quality_1080p"	varchar(999),
	"gdrive_quality_4K"	varchar(999),
	"gdrive_download_dual_audio"	varchar(999),
	"gdrive_download_hindi_dubbed"	varchar(999),
	"onedrive_quality_480p"	varchar(999),
	"onedrive_quality_720p"	varchar(999),
	"onedrive_quality_1080p"	varchar(999),
	"onedrive_quality_4K"	varchar(999),
	"onedrive_download_dual_audio"	varchar(999),
	"onedrive_download_hindi_dubbed"	varchar(999),
	"torrent"	varchar(999),
	"info1"	varchar(250),
	"info2"	varchar(250),
	"synopsys"	text,
	"subtitle_link"	varchar(999),
	"created_at"	datetime NOT NULL,
	"created_by_id"	integer,
	"last_update_id"	integer,
	"direct_download_1080p"	varchar(999),
	"direct_download_480p"	varchar(999),
	"direct_download_4K"	varchar(999),
	"direct_download_720p"	varchar(999),
	"direct_download_dual_audio"	varchar(999),
	"direct_download_hindi_dubbed"	varchar(999),
	"writers"	varchar(250),
	"tmdb_poster"	varchar(999),
	"tmdb_thumbnail"	varchar(999),
	"hevc_download_dual_audio"	varchar(999),
	"hevc_download_hindi_dubbed"	varchar(999),
	"hevc_quality_1080p"	varchar(999),
	"hevc_quality_4K"	varchar(999),
	"hevc_quality_720p"	varchar(999),
	"watch_link_main_source"	varchar(999),
	"watch_link_alt1_url"	varchar(999),
	"watch_link_alt2_url"	varchar(999),
	"watch_link_alt1_name"	varchar(250),
	"watch_link_alt2_name"	varchar(250),
	"tmdbid"	bigint UNIQUE,
	"still_path"	varchar(5000),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("created_by_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("last_update_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_episodemodel" (
	"id"	integer NOT NULL,
	"title"	varchar(250),
	"thumbnail"	varchar(100),
	"episode"	integer,
	"description"	text,
	"rating"	real,
	"runtime"	varchar(250),
	"subtitle_link"	varchar(999),
	"created_at"	datetime NOT NULL,
	"season_id"	bigint,
	"watch_link_main_source"	varchar(999),
	"direct_download_alt1_name"	varchar(250),
	"direct_download_alt1_url"	varchar(999),
	"direct_download_alt2_name"	varchar(250),
	"direct_download_alt2_url"	varchar(999),
	"gdrive_download_alt1_name"	varchar(250),
	"gdrive_download_alt1_url"	varchar(999),
	"gdrive_download_alt2_name"	varchar(250),
	"gdrive_download_alt2_url"	varchar(999),
	"onedrive_download_alt1_name"	varchar(250),
	"onedrive_download_alt1_url"	varchar(999),
	"onedrive_download_alt2_name"	varchar(250),
	"onedrive_download_alt2_url"	varchar(999),
	"watch_link_alt1_name"	varchar(250),
	"watch_link_alt1_url"	varchar(999),
	"watch_link_alt2_name"	varchar(250),
	"watch_link_alt2_url"	varchar(999),
	"direct_download_main"	varchar(999),
	"gdrive_download_main"	varchar(999),
	"onedrive_download_main"	varchar(999),
	"tmdb_thumbnail"	varchar(999),
	"hevc_download_alt1_name"	varchar(250),
	"hevc_download_alt1_url"	varchar(999),
	"hevc_download_alt2_name"	varchar(250),
	"hevc_download_alt2_url"	varchar(999),
	"hevc_download_main"	varchar(999),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("season_id") REFERENCES "core_seasonmodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_seasonmodel" (
	"id"	integer NOT NULL,
	"thumbnail"	varchar(100),
	"release_date"	date,
	"season_number"	integer,
	"episode_count"	integer,
	"complete"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"series_id"	bigint,
	"download_full_download_dual_audio"	varchar(999),
	"download_full_download_hindi_dubbed"	varchar(999),
	"download_full_quality_1080p"	varchar(999),
	"download_full_quality_480p"	varchar(999),
	"download_full_quality_720p"	varchar(999),
	"slug"	varchar(250),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("series_id") REFERENCES "core_seriesmodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_bsubcreatormodel" (
	"id"	integer NOT NULL,
	"name"	varchar(255),
	"subscene_url"	varchar(200),
	"profile_pic"	varchar(100),
	"slug"	varchar(250),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "core_moviemodel_bsub_creator" (
	"id"	integer NOT NULL,
	"moviemodel_id"	bigint NOT NULL,
	"bsubcreatormodel_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("bsubcreatormodel_id") REFERENCES "core_bsubcreatormodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("moviemodel_id") REFERENCES "core_moviemodel"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "core_seriesmodel_bsub_creator" (
	"id"	integer NOT NULL,
	"seriesmodel_id"	bigint NOT NULL,
	"bsubcreatormodel_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("seriesmodel_id") REFERENCES "core_seriesmodel"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("bsubcreatormodel_id") REFERENCES "core_bsubcreatormodel"("id") DEFERRABLE INITIALLY DEFERRED
);
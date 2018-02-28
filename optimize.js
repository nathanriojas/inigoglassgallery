const gulp = require('gulp');
const imagemin = require('gulp-imagemin');

gulp.task('default', () =>
	gulp.src('/functional/Alligator.JPG')
		.pipe(imagemin())
		.pipe(gulp.dest('/optFunctional'))
);